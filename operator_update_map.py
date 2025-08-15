#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# epicor_employee_update_map_locked.py

# - Adds a single 7-digit employee ID and full name to an INI mapping file.
# - Uses a lock file (<OutputFile>.lock) on the same share to serialize writers.
# - Writes via atomic replace so readers never see partial files.

# DEFAULT CONFIG (when --config omitted):
#   <same folder as this script>\<program_name>.ini

# Config INI:
#   [Files]
#   OutputFile = \\server\share\path\employee_id.ini

# Mapping INI format:
#   ; Maps operator ID to operator name

#   [OperatorID]
#   1234567=Donald Duck
#   1923282=Roger Anderson


import os
import sys
import json
import re
import argparse
import getpass
import logging
import configparser
import requests
import socket
import uuid
import time
import errno
import tempfile
from typing import Optional, Tuple
from urllib3.exceptions import InsecureRequestWarning

_DEBUG_ENABLED = False

# ---- Epicor ----
BAQ_BASE = "https://az-prodapp01.nortechsys.com/NSI_EPICOR/api/v1/BaqSvc/Employee"
EPICOR_CRED_FILE = os.path.expanduser("~") + "\\epicor_cred.json"
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# ---- Exit codes ----
EXIT_OK              = 0
EXIT_INVALID_ARG     = 1
EXIT_CONFIG_ERROR    = 2
EXIT_AUTH_ERROR      = 3
EXIT_HTTP_ERROR      = 4
EXIT_NOT_FOUND       = 5
EXIT_IO_ERROR        = 6

# ---------- logging ----------
def setup_logging(debug: bool):
    global _DEBUG_ENABLED
    _DEBUG_ENABLED = bool(debug)
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

# ---------- path helpers ----------
def script_dir() -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return os.path.dirname(sys.executable)
    try:
        return os.path.dirname(os.path.abspath(__file__))
    except NameError:
        return os.path.dirname(os.path.abspath(sys.argv[0]))

def default_config_path() -> str:
    base = os.path.splitext(os.path.basename(sys.argv[0]))[0] + ".ini"
    return os.path.join(script_dir(), base)

# ---------- ID + creds ----------
def scrub_emp_id(s: str) -> str:
    return re.sub(r"\D", "", s or "")

def get_creds() -> Tuple[Optional[str], Optional[str]]:
    user = os.environ.get("EPICOR_USERNAME")
    pwd  = os.environ.get("EPICOR_PASSWORD")
    if user and pwd:
        return user, pwd
    if os.path.exists(EPICOR_CRED_FILE):
        try:
            with open(EPICOR_CRED_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            user = data.get("Username")
            pwd = data.get("Password")
            if user and pwd:
                return user, pwd
        except Exception:
            pass
    # last resort: prompt
    user = input("Epicor username: ").strip()
    pwd  = getpass.getpass("Epicor password: ")
    return user, pwd

def lookup_name(emp_id: str, username: str, password: str, verify_ssl: bool=False) -> str:
    """
    Returns full name (str). Raises:
      - PermissionError on 401/403 (invalid credentials)
      - requests.HTTPError on other HTTP errors
      - ValueError if not found
    """
    params = {"$select": "EmpBasic_Name", "$filter": f"EmpBasic_EmpID eq '{emp_id}'"}
    r = requests.get(
        BAQ_BASE + "/",
        params=params,
        auth=(username, password),
        headers={"Accept": "application/json"},
        verify=verify_ssl,
        timeout=20,
    )
    if r.status_code in (401, 403):
        raise PermissionError(f"Epicor auth failed (HTTP {r.status_code}).")
    r.raise_for_status()
    data = r.json()
    vals = data.get("value", [])
    if isinstance(vals, list) and vals:
        name = vals[0].get("EmpBasic_Name")
        if isinstance(name, str) and name.strip():
            return name.strip()
    raise ValueError("Employee not found")

# ---------- config read ----------
def load_output_path_from_config(cfg_path: str) -> str:
    if not os.path.exists(cfg_path):
        raise FileNotFoundError(f"Config not found: {cfg_path}")
    cfg = configparser.ConfigParser(interpolation=None)
    cfg.read(cfg_path, encoding="utf-8")
    try:
        out_path = cfg.get("Files", "OutputFile")
    except Exception:
        raise KeyError("Config missing [Files]/OutputFile")
    if not out_path.strip():
        raise KeyError("OutputFile is empty")
    return out_path

# ---------- lock + atomic replace ----------
def _unique_owner():
    return {
        "host": socket.gethostname(),
        "pid": os.getpid(),
        "mac": f"{uuid.getnode():012x}",
        "started": time.time(),
    }

class NetworkFileLock:
    """
    Lock via atomic create (O_EXCL) of <target>.lock on same share.
    Breaks stale locks older than 'stale_after' seconds (best-effort).
    """
    def __init__(self, lock_path, timeout=45.0, poll=0.25, stale_after=300.0):
        self.lock_path = lock_path
        self.timeout = float(timeout)
        self.poll = float(poll)
        self.stale_after = float(stale_after)
        self._fd = None
        self._owner = _unique_owner()

    def __enter__(self):
        deadline = time.time() + self.timeout
        lock_dir = os.path.dirname(self.lock_path)
        if lock_dir:
            os.makedirs(lock_dir, exist_ok=True)
        while True:
            try:
                self._fd = os.open(self.lock_path, os.O_CREAT | os.O_EXCL | os.O_RDWR)
                os.write(self._fd, json.dumps(self._owner).encode("utf-8"))
                os.fsync(self._fd)
                logging.debug(f"Acquired lock {self.lock_path} as {self._owner}")
                return self
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
                # lock exists: check staleness
                try:
                    st = os.stat(self.lock_path)
                    age = time.time() - st.st_mtime
                except FileNotFoundError:
                    continue
                if age > self.stale_after:
                    stale_name = f"{self.lock_path}.stale.{int(time.time())}"
                    try:
                        os.replace(self.lock_path, stale_name)
                        logging.warning(f"Broke stale lock -> {stale_name}")
                        continue
                    except OSError:
                        pass
                if time.time() >= deadline:
                    raise TimeoutError(f"Timed out waiting for lock {self.lock_path}")
                time.sleep(self.poll)

    def __exit__(self, exc_type, exc, tb):
        try:
            if self._fd is not None:
                try:
                    os.close(self._fd)
                except OSError:
                    pass
            try:
                os.remove(self.lock_path)
            except FileNotFoundError:
                pass
            logging.debug(f"Released lock {self.lock_path}")
        finally:
            self._fd = None

def atomic_replace(path, data_bytes: bytes):
    d = os.path.dirname(path) or "."
    os.makedirs(d, exist_ok=True)
    with tempfile.NamedTemporaryFile(delete=False, dir=d) as tmp:
        tmp.write(data_bytes)
        tmp.flush()
        os.fsync(tmp.fileno())
        tmp_path = tmp.name
    os.replace(tmp_path, path)

# ---------- mapping ops (manual, preserves comments/format) ----------
HEADER_BYTES = b"; Maps operator ID to operator name\n\n[OperatorID]\n"

def mapping_contains_emp(path: str, emp_id: str) -> bool:
    if not os.path.exists(path):
        return False
    in_section = False
    try:
        with open(path, "rb") as f:
            for raw in f:
                s = raw.strip()
                if not s or s.startswith(b";"):
                    continue
                if s.startswith(b"[") and s.endswith(b"]"):
                    in_section = (s.strip().lower() == b"[operatorid]")
                    continue
                if in_section:
                    if s.split(b"=", 1)[0].strip() == emp_id.encode("utf-8"):
                        return True
    except Exception as e:
        logging.debug(f"mapping_contains_emp error: {e}")
        return False
    return False

def build_new_mapping_bytes(path: str, emp_id: str, name: str) -> bytes:
    """Return the complete new file bytes with 'emp_id=name' inserted."""
    new_line = f"{emp_id}={name}\n".encode("utf-8")

    if not os.path.exists(path):
        return HEADER_BYTES + new_line

    with open(path, "rb") as f:
        lines = f.readlines()

    sec_start = -1
    next_sec = -1
    for i, raw in enumerate(lines):
        s = raw.strip()
        if s.startswith(b"[") and s.endswith(b"]"):
            if s.strip().lower() == b"[operatorid]":
                sec_start = i
                next_sec = -1
            elif sec_start != -1 and next_sec == -1:
                next_sec = i

    if sec_start == -1:
        # Append fresh section at end
        if lines and not lines[-1].endswith(b"\n"):
            lines[-1] += b"\n"
        lines.extend([b"\n", HEADER_BYTES, new_line])
    else:
        insert_at = len(lines) if next_sec == -1 else next_sec
        if insert_at > 0 and not lines[insert_at - 1].endswith(b"\n"):
            lines[insert_at - 1] += b"\n"
        lines.insert(insert_at, new_line)

    return b"".join(lines)

def update_mapping_locked(out_map_path: str, emp_id: str, full_name: str) -> bool:
    """
    Acquire <out_map_path>.lock, re-check presence, then atomic replace with new content.
    Returns True if file changed, False if already contained emp_id.
    """
    lock_path = out_map_path + ".lock"
    with NetworkFileLock(lock_path, timeout=60, poll=0.2, stale_after=600):
        if mapping_contains_emp(out_map_path, emp_id):
            return False
        new_bytes = build_new_mapping_bytes(out_map_path, emp_id, full_name)
        atomic_replace(out_map_path, new_bytes)
        return True

def _pause_if_debug():
    """Pause on exit when --debug is set and we have an interactive console."""
    if not _DEBUG_ENABLED:
        return
    try:
        # Avoid blocking headless runs (CUP/Task Scheduler/pipes)
        if sys.stdin and sys.stdin.isatty():
            input("DEBUG: Press Enter to exit...")
    except Exception:
        pass

# ---------- main ----------
def main():
    ap = argparse.ArgumentParser(description="Add an employee ID->Name to mapping INI if missing (with network-safe locking).")
    ap.add_argument("empid", help="Employee ID (any format; digits will be extracted)")
    ap.add_argument("--config", "-c", help="Path to config INI with [Files]/OutputFile")
    ap.add_argument("--verify-ssl", action="store_true", help="Verify SSL certificates (default: off)")
    ap.add_argument("--debug", action="store_true", help="Verbose logging")
    args = ap.parse_args()

    setup_logging(args.debug)

    cfg_path = args.config if args.config else default_config_path()
    logging.debug(f"Using config: {cfg_path}")

    # Sanitize ID
    emp_id = scrub_emp_id(args.empid.strip())
    if len(emp_id) != 7:
        logging.error("Invalid employee ID (must be exactly 7 digits after scrubbing).")
        return EXIT_INVALID_ARG

    # Load mapping path
    try:
        out_map = load_output_path_from_config(cfg_path)
    except (FileNotFoundError, KeyError) as e:
        logging.error(str(e))
        return EXIT_CONFIG_ERROR
    except Exception as e:
        logging.error(f"Config error: {e}")
        return EXIT_CONFIG_ERROR

    # Fast path: already present (no lock yet, just avoid needless Epicor call)
    try:
        if mapping_contains_emp(out_map, emp_id):
            logging.info(f"{emp_id} already present in mapping. No action.")
            return EXIT_OK
    except Exception as e:
        logging.debug(f"Pre-check failed (continuing): {e}")

    # Credentials
    username, password = get_creds()
    if not username or not password:
        logging.error("Missing Epicor credentials.")
        return EXIT_AUTH_ERROR

    # Lookup
    try:
        full_name = lookup_name(emp_id, username, password, verify_ssl=args.verify_ssl)
    except PermissionError as e:
        logging.error(str(e))
        return EXIT_AUTH_ERROR
    except requests.HTTPError as e:
        logging.error(f"Epicor HTTP error: {e}")
        return EXIT_HTTP_ERROR
    except ValueError:
        logging.info("Employee not found; nothing added.")
        return EXIT_NOT_FOUND
    except Exception as e:
        logging.error(f"Lookup failed: {e}")
        return EXIT_HTTP_ERROR

    # Locked update (double-check inside lock, then atomic replace)
    try:
        changed = update_mapping_locked(out_map, emp_id, full_name)
        if changed:
            logging.info(f"Added {emp_id}={full_name} to {out_map}")
        else:
            logging.info(f"{emp_id} appeared during race; no action.")
    except TimeoutError as e:
        logging.error(str(e))
        return EXIT_IO_ERROR
    except Exception as e:
        logging.error(f"Failed to update mapping: {e}")
        return EXIT_IO_ERROR

    return EXIT_OK

if __name__ == "__main__":
    rc = main()
    _pause_if_debug()
    sys.exit(rc)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
epicor_employee_map.py
Builds an [OperatorID] mapping (INI format) from a list of 7-digit IDs
by querying Epicor BAQSvc/Employee for EmpBasic_Name.

DEFAULT CONFIG SEARCH:
- If --config/-c is omitted, looks for: <script_dir>\operator_id_mapping.ini

CONFIG FILE (INI):
------------------
[Files]
InputFile = C:\path\to\employee_ids.txt
OutputFile = C:\path\to\operator_map.ini

USAGE:
------
python epicor_employee_map.py
python epicor_employee_map.py --config C:\some\other\path.ini
python epicor_employee_map.py --reset
"""

import os
import sys
import json
import re
import argparse
import logging
import configparser
import requests
from urllib3.exceptions import InsecureRequestWarning

# ---------- Constants ----------
EPICOR_CRED_FILE = os.path.expanduser("~") + "\\epicor_cred.json"
BAQ_BASE = "https://az-prodapp01.nortechsys.com/NSI_EPICOR/api/v1/BaqSvc/Employee"

# Suppress SSL warnings if verify=False (internal certs)
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# ---------- Logging ----------
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

# ---------- Script dir helper ----------
def script_dir():
    """Directory of the running script (PyInstaller-safe), else cwd fallback."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return os.path.dirname(sys.executable)
    try:
        return os.path.dirname(os.path.abspath(__file__))
    except NameError:
        return os.getcwd()

def default_config_path():
    return os.path.join(script_dir(), "operator_id_mapping.ini")

# ---------- Credentials ----------
def load_creds(path=EPICOR_CRED_FILE):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                c = json.load(f)
            return c.get("Username"), c.get("Password")
        except Exception as e:
            logging.error(f"Failed reading credentials: {e}")
    return None, None

def save_creds(username, password, path=EPICOR_CRED_FILE):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"Username": username, "Password": password}, f)
        logging.info(f"Credentials saved to {path}")
    except Exception as e:
        logging.error(f"Failed writing credentials: {e}")
        sys.exit(1)

# ---------- Config (files INI) ----------
def load_files_config(path):
    cfg = configparser.ConfigParser()
    if not os.path.exists(path):
        logging.error(
            f"Config not found: {path}\n"
            f"Create it with:\n\n[Files]\nInputFile = C:\\path\\to\\employee_ids.txt\nOutputFile = C:\\path\\to\\operator_map.ini\n\n"
            f"Or pass a custom path with --config."
        )
        sys.exit(1)
    try:
        cfg.read(path, encoding="utf-8")
        in_path = cfg.get("Files", "InputFile")
        out_path = cfg.get("Files", "OutputFile")
        if not in_path or not out_path:
            raise KeyError
        return in_path, out_path
    except Exception:
        logging.error(
            "Config error. Expecting an INI with a [Files] section containing "
            "InputFile and OutputFile keys."
        )
        sys.exit(1)

# ---------- Epicor BAQ lookup ----------
def get_employee_name(emp_id, username, password, verify_ssl=False):
    """
    Returns the EmpBasic_Name for a given EmpBasic_EmpID (string),
    or None if not found.
    """
    params = {
        "$select": "EmpBasic_Name",
        "$filter": f"EmpBasic_EmpID eq '{emp_id}'"
    }
    try:
        resp = requests.get(
            BAQ_BASE + "/",
            params=params,
            auth=(username, password),
            headers={"Accept": "application/json"},
            verify=verify_ssl,
            timeout=20,
        )
        resp.raise_for_status()
        data = resp.json()
        records = data.get("value", [])
        if records and isinstance(records, list):
            name = records[0].get("EmpBasic_Name")
            if isinstance(name, str) and name.strip():
                return name.strip()
        return None
    except requests.HTTPError as e:
        status = getattr(e.response, "status_code", "?")
        body = getattr(e.response, "text", "")[:200]
        logging.error(f"{emp_id}: HTTP {status} - {body}")
        return None
    except Exception as e:
        logging.error(f"{emp_id}: request failed - {e}")
        return None

# ---------- I/O ----------
def read_ids(path):
    if not os.path.exists(path):
        logging.error(f"Input file not found: {path}")
        sys.exit(1)

    ids = []
    seen = set()
    with open(path, "r", encoding="utf-8") as f:
        for ln, raw in enumerate(f, 1):
            s = raw.strip()
            if not s:
                continue
            if not re.fullmatch(r"\d{7}", s):
                logging.warning(f"Line {ln}: invalid ID '{s}' (must be exactly 7 digits) - skipped")
                continue
            if s in seen:
                continue
            seen.add(s)
            ids.append(s)
    if not ids:
        logging.error("No valid 7-digit IDs found in input.")
        sys.exit(1)
    return ids

def write_ini_mapping(path, id_to_name, header_comment="; Maps operator ID to operator name"):
    out_dir = os.path.dirname(path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{header_comment}\n\n[OperatorID]\n")
        for emp_id in id_to_name["order"]:  # preserve input order
            name = id_to_name["map"].get(emp_id)
            if name:
                f.write(f"{emp_id}={name}\n")
    wrote = sum(1 for _ in id_to_name["map"].values() if _)
    logging.info(f"Wrote {wrote} mappings to {path}")

# ---------- Main ----------
def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Build [OperatorID] mapping from Epicor BAQ Employee lookup.")
    parser.add_argument("--config", "-c",
                        help=f"Path to INI with [Files] InputFile/OutputFile "
                             f"(default: {default_config_path()})")
    parser.add_argument("--reset", action="store_true", help="Re-enter and save Epicor credentials")
    parser.add_argument("--verify-ssl", action="store_true", help="Verify SSL certificates (default: off)")
    args = parser.parse_args()

    cfg_path = args.config if args.config else default_config_path()
    logging.info(f"Using config: {cfg_path}")

    in_file, out_file = load_files_config(cfg_path)

    username, password = load_creds()
    if args.reset or not username or not password:
        import getpass
        username = input("Epicor username: ").strip()
        password = getpass.getpass("Epicor password: ")
        if not username or not password:
            logging.error("Username/password are required.")
            sys.exit(1)
        save_creds(username, password)

    ids = read_ids(in_file)

    id_to_name_map = {}
    for idx, emp_id in enumerate(ids, 1):
        name = get_employee_name(emp_id, username, password, verify_ssl=args.verify_ssl)
        if name:
            logging.info(f"[{idx}/{len(ids)}] {emp_id} -> {name}")
            id_to_name_map[emp_id] = name
        else:
            logging.warning(f"[{idx}/{len(ids)}] {emp_id} -> NOT FOUND")

    if not any(id_to_name_map.values()):
        logging.error("No IDs resolved to names. Nothing to write.")
        sys.exit(2)

    write_ini_mapping(out_file, {"order": ids, "map": id_to_name_map})

if __name__ == "__main__":
    main()

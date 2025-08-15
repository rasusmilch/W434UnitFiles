#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
epicor_employee_lookup_cli.py

Usage:
  python epicor_employee_lookup_cli.py 3266670
  python epicor_employee_lookup_cli.py --verify-ssl 3266670

Behavior:
- Scrubs the provided argument to digits only.
- If not exactly 7 digits after scrubbing => prints "NULL".
- Calls Epicor BAQ to get EmpBasic_Name for that ID.
- Prints the name if found, else "NULL".

Credentials:
- Tries environment vars EPICOR_USERNAME / EPICOR_PASSWORD first.
- Else tries %USERPROFILE%\\epicor_cred.json with {"Username": "...", "Password": "..."}.
- Else prompts.
"""

import os
import sys
import json
import re
import argparse
import getpass
import requests
from urllib3.exceptions import InsecureRequestWarning

BAQ_BASE = "https://az-prodapp01.nortechsys.com/NSI_EPICOR/api/v1/BaqSvc/Employee"
EPICOR_CRED_FILE = os.path.expanduser("~") + "\\epicor_cred.json"

# Suppress warnings if we’re not verifying SSL (internal certs, etc.)
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def scrub_emp_id(s: str) -> str:
    """Return digits-only string from input."""
    return re.sub(r"\D", "", s or "")

def get_creds():
    """Load Epicor creds from env, then file, else prompt."""
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
            pass  # fall through to prompt

    # prompt as last resort (no echo for password)
    user = input("Epicor username: ").strip()
    pwd  = getpass.getpass("Epicor password: ")
    return user, pwd

def lookup_name(emp_id: str, username: str, password: str, verify_ssl: bool=False) -> str | None:
    """Return full name for employee ID or None if not found/error."""
    params = {
        "$select": "EmpBasic_Name",
        "$filter": f"EmpBasic_EmpID eq '{emp_id}'"
    }
    try:
        r = requests.get(
            BAQ_BASE + "/",
            params=params,
            auth=(username, password),
            headers={"Accept": "application/json"},
            verify=verify_ssl,
            timeout=20,
        )
        r.raise_for_status()
        data = r.json()
        vals = data.get("value", [])
        if isinstance(vals, list) and vals:
            name = vals[0].get("EmpBasic_Name")
            if isinstance(name, str) and name.strip():
                return name.strip()
        return None
    except Exception:
        return None

def main():
    p = argparse.ArgumentParser(description="Print Epicor employee name for a given 7-digit ID, or NULL.")
    p.add_argument("empid", help="Employee ID (any format; digits will be extracted)")
    p.add_argument("--verify-ssl", action="store_true", help="Verify SSL certificates (default: off)")
    args = p.parse_args()

    raw = args.empid.strip()
    emp_id = scrub_emp_id(raw)

    # sanity checks
    if len(emp_id) != 7:
        print("NULL")
        return 0

    username, password = get_creds()
    if not username or not password:
        # If still missing (e.g., user just hit enter), treat as failure
        print("NULL")
        return 0

    name = lookup_name(emp_id, username, password, verify_ssl=args.verify_ssl)
    print(name if name else "NULL")
    return 0

if __name__ == "__main__":
    sys.exit(main())

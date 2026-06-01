#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
epicor_employee_lookup.py

Usage:
  python epicor_employee_lookup.py 3266670
  python epicor_employee_lookup.py --verify-ssl 3266670
  python epicor_employee_lookup.py gui
  python epicor_employee_lookup.py --verify-ssl gui
  python epicor_employee_lookup.py reset-creds

Behavior:
- Command line mode is the default.
- Passing "gui" as the employee ID/command launches a small Tkinter GUI.
- Passing "reset-creds" resets saved credentials and prompts for new ones.
- Employee IDs are scrubbed to digits only.
- If the scrubbed employee ID is not exactly 7 digits, CLI mode prints "NULL".
- Calls the Epicor BAQ to get EmpBasic_Name for that ID.
- Prints the name if found; otherwise prints "NULL".

Credentials:
- Uses ~/epicor_cred.json with {"Username": "...", "Password": "..."}.
- If credentials are missing, the CLI prompts for them and saves them.
- If credentials are missing, the GUI prompts for them and saves them.
- Credentials can be reset from CLI or GUI when an Epicor password changes.
- Environment variables are intentionally not used.
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re
import sys
import threading

import requests
from requests import Response
from urllib3.exceptions import InsecureRequestWarning

BAQ_BASE = "https://az-prodapp01.nortechsys.com/NSI_EPICOR/api/v1/BaqSvc/Employee"
EPICOR_CRED_FILE = Path.home() / "epicor_cred.json"
EMPLOYEE_ID_DIGITS = 7
REQUEST_TIMEOUT_SECONDS = 20

# Suppress warnings if SSL verification is disabled. This script normally talks
# to an internal Epicor endpoint where certificate validation may not be set up
# for every workstation.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


@dataclass(frozen=True)
class Credentials:
    """Epicor username and password."""

    username: str
    password: str


@dataclass(frozen=True)
class CredentialLoadResult:
    """Credential file load result with an operator-facing message."""

    credentials: Credentials | None
    message: str | None = None


@dataclass(frozen=True)
class LookupResult:
    """Employee lookup result with an operator-facing message."""

    employee_id: str
    name: str | None
    message: str
    is_error: bool = False


class EmployeeLookupGui:
    """Tkinter GUI wrapper for Epicor employee lookup."""

    def __init__(self, tk_module, messagebox_module, simpledialog_module,
                 scrolledtext_module, verify_ssl: bool) -> None:
        """Initialize the GUI widgets and state.

        Args:
            tk_module: Imported tkinter module.
            messagebox_module: Imported tkinter.messagebox module.
            simpledialog_module: Imported tkinter.simpledialog module.
            scrolledtext_module: Imported tkinter.scrolledtext module.
            verify_ssl: True to verify SSL certificates for Epicor requests.

        Returns:
            None.
        """
        self.tk = tk_module
        self.messagebox = messagebox_module
        self.simpledialog = simpledialog_module
        self.scrolledtext = scrolledtext_module
        self.verify_ssl = verify_ssl
        self.root = self.tk.Tk()
        self.root.title("Epicor Employee Lookup")
        self.root.resizable(width=False, height=False)

        self.employee_number_var = self.tk.StringVar()
        self.result_var = self.tk.StringVar(value="Enter an employee number.")
        self.status_var = self.tk.StringVar(value=f"Credential file: {EPICOR_CRED_FILE}")

        self.lookup_button = None
        self.history_text = None
        self._build_widgets()
        self.root.after(100, self._prompt_for_missing_credentials_on_startup)

    def _build_widgets(self) -> None:
        """Create and place all main window widgets.

        Args:
            None.

        Returns:
            None.
        """
        main_frame = self.tk.Frame(self.root, padx=12, pady=12)
        main_frame.grid(row=0, column=0, sticky="nsew")

        employee_label = self.tk.Label(main_frame, text="Employee number:")
        employee_label.grid(row=0, column=0, sticky="w")

        employee_entry = self.tk.Entry(
            main_frame,
            textvariable=self.employee_number_var,
            width=24,
        )
        employee_entry.grid(row=1, column=0, sticky="ew", pady=(2, 8))
        employee_entry.bind("<Return>", lambda unused_event: self.lookup_employee())
        employee_entry.focus_set()

        button_frame = self.tk.Frame(main_frame)
        button_frame.grid(row=1, column=1, sticky="e", padx=(8, 0), pady=(2, 8))

        self.lookup_button = self.tk.Button(
            button_frame,
            text="Lookup",
            width=12,
            command=self.lookup_employee,
        )
        self.lookup_button.grid(row=0, column=0, padx=(0, 6))

        reset_credentials_button = self.tk.Button(
            button_frame,
            text="Reset Creds",
            width=12,
            command=self.reset_credentials,
        )
        reset_credentials_button.grid(row=0, column=1)

        result_label = self.tk.Label(
            main_frame,
            textvariable=self.result_var,
            anchor="w",
            justify="left",
            width=58,
        )
        result_label.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 8))

        history_label = self.tk.Label(main_frame, text="Lookup history:")
        history_label.grid(row=3, column=0, columnspan=2, sticky="w")

        self.history_text = self.scrolledtext.ScrolledText(
            main_frame,
            width=64,
            height=10,
            state="disabled",
            wrap="word",
        )
        self.history_text.grid(row=4, column=0, columnspan=2, sticky="ew")

        status_label = self.tk.Label(
            main_frame,
            textvariable=self.status_var,
            anchor="w",
            justify="left",
            width=58,
        )
        status_label.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(8, 0))

    def run(self) -> int:
        """Run the Tkinter event loop.

        Args:
            None.

        Returns:
            Process exit code.
        """
        self.root.mainloop()
        return 0

    def _prompt_for_missing_credentials_on_startup(self) -> None:
        """Prompt for credentials at startup when no complete file exists.

        Args:
            None.

        Returns:
            None.
        """
        credential_load_result = load_saved_credentials()
        if credential_load_result.credentials:
            return

        if credential_load_result.message:
            self.status_var.set(credential_load_result.message)

        self.prompt_and_save_credentials()

    def prompt_and_save_credentials(self) -> Credentials | None:
        """Prompt the operator for credentials and save them to disk.

        Args:
            None.

        Returns:
            Saved credentials, or None if the prompt was canceled or invalid.
        """
        username = self.simpledialog.askstring(
            "Epicor Credentials",
            "Epicor username:",
            parent=self.root,
        )
        if username is None:
            self.status_var.set("Credential entry canceled. Lookup requires an Epicor username and password.")
            return None

        password = self.simpledialog.askstring(
            "Epicor Credentials",
            "Epicor password:",
            parent=self.root,
            show="*",
        )
        if password is None:
            self.status_var.set("Credential entry canceled. Lookup requires an Epicor username and password.")
            return None

        credentials = Credentials(username=username.strip(), password=password)
        if not credentials.username or not credentials.password:
            self.messagebox.showerror(
                "Missing Credentials",
                "Epicor username and password are both required.",
            )
            self.status_var.set("Credentials were not saved because one or more fields were blank.")
            return None

        save_error_message = save_credentials(credentials)
        if save_error_message:
            self.messagebox.showwarning(
                "Credential Save Failed",
                save_error_message,
            )
            self.status_var.set(save_error_message)
            return credentials

        self.status_var.set(f"Credentials saved to {EPICOR_CRED_FILE}")
        return credentials

    def reset_credentials(self) -> Credentials | None:
        """Reset saved credentials and prompt the operator for new credentials.

        Args:
            None.

        Returns:
            Saved replacement credentials, or None if the reset was canceled or invalid.
        """
        should_reset = self.messagebox.askyesno(
            "Reset Epicor Credentials",
            "Reset saved Epicor credentials and enter a new username and password?",
        )
        if not should_reset:
            self.status_var.set("Credential reset canceled.")
            return None

        reset_error_message = reset_saved_credentials()
        if reset_error_message:
            self.messagebox.showwarning("Credential Reset Warning", reset_error_message)
            self.status_var.set(reset_error_message)
        else:
            self.status_var.set("Saved credentials were reset. Enter new Epicor credentials.")

        return self.prompt_and_save_credentials()

    def lookup_employee(self) -> None:
        """Start an employee lookup from the GUI input box.

        Args:
            None.

        Returns:
            None.
        """
        raw_employee_id = self.employee_number_var.get().strip()
        employee_id = scrub_employee_id(raw_employee_id)

        if len(employee_id) != EMPLOYEE_ID_DIGITS:
            message = "Employee number must contain exactly 7 digits."
            self.result_var.set(message)
            self.status_var.set(message)
            self._append_history(raw_employee_id or "<blank>", "INVALID", message)
            return

        credential_load_result = load_saved_credentials()
        credentials = credential_load_result.credentials
        if credentials is None:
            if credential_load_result.message:
                self.status_var.set(credential_load_result.message)
            credentials = self.prompt_and_save_credentials()
            if credentials is None:
                message = "Lookup canceled. Epicor credentials are required."
                self.result_var.set(message)
                self._append_history(employee_id, "ERROR", message)
                return

        self.result_var.set(f"Looking up employee {employee_id}...")
        self.status_var.set("Epicor lookup in progress.")
        self.lookup_button.configure(state="disabled")

        lookup_thread = threading.Thread(
            target=self._lookup_worker,
            args=(employee_id, credentials),
            daemon=True,
        )
        lookup_thread.start()

    def _lookup_worker(self, employee_id: str, credentials: Credentials) -> None:
        """Run the network lookup outside the Tkinter event loop.

        Args:
            employee_id: Seven-digit employee ID.
            credentials: Epicor credentials to use.

        Returns:
            None.
        """
        lookup_result = lookup_name(
            employee_id=employee_id,
            credentials=credentials,
            verify_ssl=self.verify_ssl,
        )
        self.root.after(0, lambda: self._handle_lookup_result(lookup_result))

    def _handle_lookup_result(self, lookup_result: LookupResult) -> None:
        """Display a completed lookup result.

        Args:
            lookup_result: Result returned by lookup_name().

        Returns:
            None.
        """
        self.lookup_button.configure(state="normal")

        if lookup_result.name:
            self.result_var.set(lookup_result.name)
            self.status_var.set(lookup_result.message)
            self._append_history(lookup_result.employee_id, lookup_result.name, lookup_result.message)
            return

        if lookup_result.is_error:
            self.result_var.set("Lookup failed.")
            self.status_var.set(lookup_result.message)
            self._append_history(lookup_result.employee_id, "ERROR", lookup_result.message)
            self.messagebox.showerror("Lookup Failed", lookup_result.message)
            return

        self.result_var.set("NULL")
        self.status_var.set(lookup_result.message)
        self._append_history(lookup_result.employee_id, "NULL", lookup_result.message)

    def _append_history(self, employee_id: str, result_text: str, message: str) -> None:
        """Append one row to the lookup history text area.

        Args:
            employee_id: Employee ID or raw input label to show.
            result_text: Lookup result summary.
            message: Operator-facing detail message.

        Returns:
            None.
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_line = f"[{timestamp}] {employee_id} -> {result_text} ({message})\n"
        self.history_text.configure(state="normal")
        self.history_text.insert("end", history_line)
        self.history_text.see("end")
        self.history_text.configure(state="disabled")


def scrub_employee_id(employee_id_text: str) -> str:
    """Return only digits from an employee ID input string.

    Args:
        employee_id_text: Raw employee ID text from CLI or GUI input.

    Returns:
        Digits-only employee ID text.
    """
    return re.sub(r"\D", "", employee_id_text or "")


def load_saved_credentials() -> CredentialLoadResult:
    """Load Epicor credentials from the local credential file.

    Args:
        None.

    Returns:
        CredentialLoadResult containing credentials or an operator-facing message.
    """
    if not EPICOR_CRED_FILE.exists():
        return CredentialLoadResult(
            credentials=None,
            message=f"Credential file was not found: {EPICOR_CRED_FILE}",
        )

    try:
        with EPICOR_CRED_FILE.open("r", encoding="utf-8") as credential_file:
            credential_data = json.load(credential_file)
    except json.JSONDecodeError as error:
        return CredentialLoadResult(
            credentials=None,
            message=f"Credential file is not valid JSON: {error}",
        )
    except OSError as error:
        return CredentialLoadResult(
            credentials=None,
            message=f"Credential file could not be read: {error}",
        )

    username = str(credential_data.get("Username") or "").strip()
    password = str(credential_data.get("Password") or "")
    if not username or not password:
        return CredentialLoadResult(
            credentials=None,
            message="Credential file is missing Username or Password.",
        )

    return CredentialLoadResult(credentials=Credentials(username=username, password=password))


def save_credentials(credentials: Credentials) -> str | None:
    """Save Epicor credentials to the local credential file.

    Args:
        credentials: Credentials to persist.

    Returns:
        None on success, or an operator-facing error message on failure.
    """
    credential_data = {
        "Username": credentials.username,
        "Password": credentials.password,
    }

    try:
        EPICOR_CRED_FILE.parent.mkdir(parents=True, exist_ok=True)
        with EPICOR_CRED_FILE.open("w", encoding="utf-8") as credential_file:
            json.dump(credential_data, credential_file, indent=2)
            credential_file.write("\n")
        try:
            os.chmod(EPICOR_CRED_FILE, 0o600)
        except OSError:
            # Permission tightening is best-effort on Windows and managed shares.
            pass
    except OSError as error:
        return f"Credentials could not be saved to {EPICOR_CRED_FILE}: {error}"

    return None

def reset_saved_credentials() -> str | None:
    """Delete the saved Epicor credential file when it exists.

    Args:
        None.

    Returns:
        None on success, or an operator-facing error message on failure.
    """
    try:
        EPICOR_CRED_FILE.unlink(missing_ok=True)
    except OSError as error:
        return f"Saved credentials could not be reset at {EPICOR_CRED_FILE}: {error}"

    return None


def reset_cli_credentials() -> int:
    """Reset saved CLI credentials and prompt for replacement credentials.

    Args:
        None.

    Returns:
        Process exit code.
    """
    reset_error_message = reset_saved_credentials()
    if reset_error_message:
        print(reset_error_message, file=sys.stderr)
        print("Credentials were not reset.", file=sys.stderr)
        return 1

    print("Saved Epicor credentials were reset. Enter replacement credentials.", file=sys.stderr)
    credentials = prompt_and_save_cli_credentials()
    if credentials is None:
        print("Replacement credentials were not saved.", file=sys.stderr)
        return 1

    print("Replacement credentials were saved.", file=sys.stderr)
    return 0


def prompt_and_save_cli_credentials() -> Credentials | None:
    """Prompt for Epicor credentials in CLI mode and save them.

    Args:
        None.

    Returns:
        Credentials entered by the operator, or None when incomplete.
    """
    try:
        username = input("Epicor username: ").strip()
        password = getpass.getpass("Epicor password: ")
    except (EOFError, KeyboardInterrupt):
        print("Credential entry canceled. Lookup requires an Epicor username and password.", file=sys.stderr)
        return None

    credentials = Credentials(username=username, password=password)
    if not credentials.username or not credentials.password:
        print("Epicor username and password are both required.", file=sys.stderr)
        return None

    save_error_message = save_credentials(credentials)
    if save_error_message:
        print(save_error_message, file=sys.stderr)
    else:
        print(f"Credentials saved to {EPICOR_CRED_FILE}", file=sys.stderr)

    return credentials


def get_cli_credentials() -> Credentials | None:
    """Load saved credentials or prompt the CLI operator.

    Args:
        None.

    Returns:
        Credentials when available, otherwise None.
    """
    credential_load_result = load_saved_credentials()
    if credential_load_result.credentials:
        return credential_load_result.credentials

    if credential_load_result.message:
        print(credential_load_result.message, file=sys.stderr)

    return prompt_and_save_cli_credentials()


def lookup_name(employee_id: str, credentials: Credentials, verify_ssl: bool = False) -> LookupResult:
    """Return the Epicor employee name lookup result.

    Args:
        employee_id: Seven-digit Epicor employee ID.
        credentials: Epicor credentials.
        verify_ssl: True to verify SSL certificates.

    Returns:
        LookupResult containing a name, not-found message, or error message.
    """
    query_params = {
        "$select": "EmpBasic_Name",
        "$filter": f"EmpBasic_EmpID eq '{employee_id}'",
    }

    try:
        response = requests.get(
            BAQ_BASE + "/",
            params=query_params,
            auth=(credentials.username, credentials.password),
            headers={"Accept": "application/json"},
            verify=verify_ssl,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        return parse_lookup_response(employee_id, response)
    except requests.exceptions.Timeout:
        return LookupResult(
            employee_id=employee_id,
            name=None,
            message="Epicor lookup timed out. Check the network/VPN connection and try again.",
            is_error=True,
        )
    except requests.exceptions.ConnectionError as error:
        return LookupResult(
            employee_id=employee_id,
            name=None,
            message=f"Could not connect to Epicor. Check the network/VPN connection. Details: {error}",
            is_error=True,
        )
    except requests.exceptions.RequestException as error:
        return LookupResult(
            employee_id=employee_id,
            name=None,
            message=f"Epicor request failed before a valid response was received. Details: {error}",
            is_error=True,
        )


def parse_lookup_response(employee_id: str, response: Response) -> LookupResult:
    """Parse the Epicor BAQ HTTP response into a lookup result.

    Args:
        employee_id: Seven-digit Epicor employee ID.
        response: requests Response returned from Epicor.

    Returns:
        LookupResult containing a name, not-found message, or error message.
    """
    if response.status_code in (401, 403):
        return LookupResult(
            employee_id=employee_id,
            name=None,
            message=(
                "Epicor rejected the username or password. "
                "Reset saved credentials and enter the updated Epicor username/password."
            ),
            is_error=True,
        )

    if not response.ok:
        return LookupResult(
            employee_id=employee_id,
            name=None,
            message=f"Epicor returned HTTP {response.status_code}: {response.reason}",
            is_error=True,
        )

    try:
        response_data = response.json()
    except ValueError as error:
        return LookupResult(
            employee_id=employee_id,
            name=None,
            message=f"Epicor returned a response that was not valid JSON: {error}",
            is_error=True,
        )

    values = response_data.get("value", [])
    if isinstance(values, list) and values:
        name = values[0].get("EmpBasic_Name")
        if isinstance(name, str) and name.strip():
            clean_name = name.strip()
            return LookupResult(
                employee_id=employee_id,
                name=clean_name,
                message=f"Employee {employee_id} found.",
            )

    return LookupResult(
        employee_id=employee_id,
        name=None,
        message=f"Employee {employee_id} was not found.",
    )


def run_cli_lookup(raw_employee_id: str, verify_ssl: bool = False) -> int:
    """Run one command line employee lookup.

    Args:
        raw_employee_id: Raw employee ID text from the command line.
        verify_ssl: True to verify SSL certificates.

    Returns:
        Process exit code.
    """
    employee_id = scrub_employee_id(raw_employee_id.strip())
    if len(employee_id) != EMPLOYEE_ID_DIGITS:
        print("NULL")
        print("Employee number must contain exactly 7 digits after removing punctuation.", file=sys.stderr)
        return 0

    credentials = get_cli_credentials()
    if credentials is None:
        print("NULL")
        return 1

    lookup_result = lookup_name(employee_id, credentials, verify_ssl=verify_ssl)
    print(lookup_result.name if lookup_result.name else "NULL")

    if lookup_result.message:
        print(lookup_result.message, file=sys.stderr)

    return 1 if lookup_result.is_error else 0


def run_gui(verify_ssl: bool = False) -> int:
    """Launch the employee lookup GUI.

    Args:
        verify_ssl: True to verify SSL certificates.

    Returns:
        Process exit code.
    """
    try:
        import tkinter as tk
        from tkinter import messagebox, simpledialog, scrolledtext
    except ImportError as error:
        print(f"The GUI requires Tkinter, but Tkinter is not available: {error}", file=sys.stderr)
        return 1

    try:
        app = EmployeeLookupGui(
            tk_module=tk,
            messagebox_module=messagebox,
            simpledialog_module=simpledialog,
            scrolledtext_module=scrolledtext,
            verify_ssl=verify_ssl,
        )
    except tk.TclError as error:
        print(f"The GUI could not be started: {error}", file=sys.stderr)
        return 1

    return app.run()


def build_arg_parser() -> argparse.ArgumentParser:
    """Build the command line argument parser.

    Args:
        None.

    Returns:
        Configured argparse.ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        description="Epicor employee name lookup.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  Lookup employee 3266670 from the command line:\n"
            "    python employee_lookup_gui.py 3266670\n\n"
            "  Launch the employee lookup window:\n"
            "    python employee_lookup_gui.py gui\n\n"
            "  Reset saved Epicor credentials and enter replacement credentials:\n"
            "    python employee_lookup_gui.py reset-creds\n\n"
            "  Use SSL certificate verification:\n"
            "    python employee_lookup_gui.py --verify-ssl 3266670\n"
            "    python employee_lookup_gui.py --verify-ssl gui\n\n"
            "Notes:\n"
            "  Employee numbers must contain exactly 7 digits after punctuation is removed.\n"
            f"  Credentials are saved in {EPICOR_CRED_FILE}.\n"
            "  Environment variables are not used for credentials.\n"
            "  Use 'reset-creds' or the GUI Reset Creds button when an Epicor password changes.\n"
        ),
    )
    parser.add_argument(
        "command_or_empid",
        nargs="?",
        help="Employee ID for CLI lookup, or 'gui' to launch the GUI.",
    )
    parser.add_argument(
        "--verify-ssl",
        action="store_true",
        help="Verify SSL certificates. Default is off for internal Epicor certificates.",
    )
    return parser


def print_missing_command_help(parser: argparse.ArgumentParser) -> None:
    """Print operator-facing help when no employee ID or GUI command was provided.

    Args:
        parser: Configured argument parser.

    Returns:
        None.
    """
    print(
        "No employee number or command was provided.\n"
        "\n"
        "To look up an employee from the command line:\n"
        "  python employee_lookup_gui.py 3266670\n"
        "\n"
        "To launch the lookup window:\n"
        "  python employee_lookup_gui.py gui\n"
        "\n"
        "To reset saved Epicor credentials:\n"
        "  python employee_lookup_gui.py reset-creds\n"
        "\n"
        "For all options:\n"
        "  python employee_lookup_gui.py --help\n"
    )


def main() -> int:
    """Parse command line arguments and run CLI or GUI mode.

    Args:
        None.

    Returns:
        Process exit code.
    """
    parser = build_arg_parser()
    args = parser.parse_args()

    if not args.command_or_empid:
        print_missing_command_help(parser)
        return 2

    command_or_empid = args.command_or_empid.lower()
    if command_or_empid == "gui":
        return run_gui(verify_ssl=args.verify_ssl)

    if command_or_empid in ("reset-creds", "reset-credentials"):
        return reset_cli_credentials()

    return run_cli_lookup(
        raw_employee_id=args.command_or_empid,
        verify_ssl=args.verify_ssl,
    )


if __name__ == "__main__":
    sys.exit(main())

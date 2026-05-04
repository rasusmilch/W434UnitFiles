#!/usr/bin/env python3
"""Find today's W434 reports that have parameters but appear to lack test rows.

This walks a directory recursively, finds text reports from a selected date
source, and flags files that contain parameter sections but no detailed
measurement/result rows.

Filename date mode expects report names ending in:

    YYYYMMDD-HHMMSS.txt

Example:

    AS-0195-001_PRETEST-A0551-20260504-122319.txt
"""

from __future__ import annotations

import argparse
import datetime as datetime_module
import os
import re
import sys
from pathlib import Path

from tqdm import tqdm


PARAMETER_SECTION_PATTERN = re.compile(
    r"^\s*Parameters for .+ test\s*$",
    re.IGNORECASE | re.MULTILINE,
)

DETAILED_RESULT_ROW_PATTERN = re.compile(
    r"^\s*(Passed|Failed|Aborted|Error|Arc|Short|Open)\s{2,}\S+",
    re.IGNORECASE | re.MULTILINE,
)

FILENAME_TIMESTAMP_PATTERN = re.compile(
    r"(?P<date>\d{8})-(?P<time>\d{6})\.txt$",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed argparse namespace.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Walk a directory recursively and list W434 text reports that "
            "contain parameter sections but appear to be missing detailed "
            "test result rows."
        )
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="Root directory to scan recursively.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help=(
            "Output text file path. Defaults to "
            "w434_missing_test_rows_YYYYMMDD.txt in the current directory."
        ),
    )
    parser.add_argument(
        "--date",
        type=str,
        default=None,
        help=(
            "Date to scan in YYYY-MM-DD format. Defaults to today's local date."
        ),
    )
    parser.add_argument(
        "--date-source",
        choices=("created", "modified", "filename"),
        default="created",
        help=(
            "How to decide whether a file belongs to the target date. "
            "Use 'filename' for W434 archive names ending in YYYYMMDD-HHMMSS.txt. "
            "Default: created."
        ),
    )
    parser.add_argument(
        "--all-extensions",
        action="store_true",
        help="Scan all files instead of only .txt files.",
    )
    return parser.parse_args()


def parse_target_date(date_text: str | None) -> datetime_module.date:
    """Parse the target date.

    Args:
        date_text: Optional date string in YYYY-MM-DD format.

    Returns:
        Target local date.

    Raises:
        ValueError: If date_text is not in YYYY-MM-DD format.
    """
    if date_text is None:
        return datetime_module.date.today()

    return datetime_module.date.fromisoformat(date_text)


def get_local_file_datetime(
    file_path: Path,
    date_source: str,
) -> datetime_module.datetime | None:
    """Return the local datetime used for filtering.

    Args:
        file_path: File path to inspect.
        date_source: One of created, modified, or filename.

    Returns:
        Local datetime from the selected file timestamp, or None when filename
        mode is selected and the filename does not contain a parsable timestamp.
    """
    if date_source == "filename":
        return get_datetime_from_filename(file_path)

    file_stat = file_path.stat()

    if date_source == "modified":
        timestamp = file_stat.st_mtime
    else:
        # On Windows this is creation time. On many Unix-like systems this is
        # metadata-change time, not true creation time.
        timestamp = file_stat.st_ctime

    return datetime_module.datetime.fromtimestamp(timestamp)


def get_datetime_from_filename(file_path: Path) -> datetime_module.datetime | None:
    """Parse a W434 archive timestamp from a filename.

    Args:
        file_path: File path whose name should end in YYYYMMDD-HHMMSS.txt.

    Returns:
        Parsed datetime, or None if the filename does not match the expected
        pattern.
    """
    match = FILENAME_TIMESTAMP_PATTERN.search(file_path.name)
    if match is None:
        return None

    timestamp_text = f"{match.group('date')}{match.group('time')}"

    try:
        return datetime_module.datetime.strptime(timestamp_text, "%Y%m%d%H%M%S")
    except ValueError:
        return None


def is_from_target_date(
    file_path: Path,
    target_date: datetime_module.date,
    date_source: str,
) -> bool:
    """Return whether the selected file date matches the target date.

    Args:
        file_path: File path to inspect.
        target_date: Local date to compare against.
        date_source: One of created, modified, or filename.

    Returns:
        True if the selected file date matches the target date.
    """
    try:
        file_datetime = get_local_file_datetime(file_path, date_source)
    except OSError:
        return False

    if file_datetime is None:
        return False

    return file_datetime.date() == target_date


def collect_target_date_files(
    root_directory: Path,
    target_date: datetime_module.date,
    all_extensions: bool,
    date_source: str,
) -> list[Path]:
    """Collect candidate files from the target date.

    Args:
        root_directory: Directory to walk recursively.
        target_date: Local date to match.
        all_extensions: When true, scan all files instead of only .txt files.
        date_source: One of created, modified, or filename.

    Returns:
        List of candidate file paths.
    """
    target_date_files: list[Path] = []

    progress_bar = tqdm(
        desc="Walking files",
        unit="file",
        dynamic_ncols=True,
    )

    def handle_walk_error(error: OSError) -> None:
        print(f"WARNING: Could not access {error.filename}: {error}", file=sys.stderr)

    for current_directory, _, filenames in os.walk(root_directory, onerror=handle_walk_error):
        current_directory_path = Path(current_directory)

        for filename in filenames:
            progress_bar.update(1)

            file_path = current_directory_path / filename

            if not all_extensions and file_path.suffix.lower() != ".txt":
                continue

            if not file_path.is_file():
                continue

            if is_from_target_date(file_path, target_date, date_source):
                target_date_files.append(file_path)

    progress_bar.close()
    return target_date_files


def read_text_file(file_path: Path) -> str | None:
    """Read a text file defensively.

    Args:
        file_path: Text file path.

    Returns:
        File contents, or None if the file could not be read.
    """
    encodings_to_try = ("utf-8", "cp1252", "latin-1")

    for encoding_name in encodings_to_try:
        try:
            return file_path.read_text(encoding=encoding_name, errors="replace")
        except OSError:
            return None
        except UnicodeError:
            continue

    return None


def has_parameters_without_test_rows(report_text: str) -> bool:
    """Return whether a report appears to have parameters but no test rows.

    Args:
        report_text: Full text report contents.

    Returns:
        True if parameter sections exist and detailed result rows appear absent.
    """
    has_parameter_sections = PARAMETER_SECTION_PATTERN.search(report_text) is not None
    has_detailed_result_rows = DETAILED_RESULT_ROW_PATTERN.search(report_text) is not None

    return has_parameter_sections and not has_detailed_result_rows


def find_suspect_reports(candidate_files: list[Path]) -> list[Path]:
    """Find reports that appear to be missing detailed test rows.

    Args:
        candidate_files: Candidate files from the selected date.

    Returns:
        Sorted list of suspect report paths.
    """
    suspect_reports: list[Path] = []

    for file_path in tqdm(candidate_files, desc="Checking reports", unit="file", dynamic_ncols=True):
        report_text = read_text_file(file_path)

        if report_text is None:
            print(f"WARNING: Could not read {file_path}", file=sys.stderr)
            continue

        if has_parameters_without_test_rows(report_text):
            suspect_reports.append(file_path)

    return sorted(suspect_reports, key=lambda path: str(path).lower())


def write_results(output_path: Path, suspect_reports: list[Path]) -> None:
    """Write suspect report paths to a text file.

    Args:
        output_path: Output text file path.
        suspect_reports: Suspect report paths to write.
    """
    output_lines = [str(report_path) for report_path in suspect_reports]
    output_text = "\n".join(output_lines)

    if output_text:
        output_text += "\n"

    output_path.write_text(output_text, encoding="utf-8")


def main() -> int:
    """Run the report scan.

    Returns:
        Process exit code.
    """
    args = parse_args()

    try:
        target_date = parse_target_date(args.date)
    except ValueError:
        print("ERROR: --date must be in YYYY-MM-DD format.", file=sys.stderr)
        return 2

    root_directory = args.directory
    if not root_directory.exists():
        print(f"ERROR: Directory does not exist: {root_directory}", file=sys.stderr)
        return 2

    if not root_directory.is_dir():
        print(f"ERROR: Path is not a directory: {root_directory}", file=sys.stderr)
        return 2

    if args.output is None:
        date_stamp = target_date.strftime("%Y%m%d")
        output_path = Path.cwd() / f"w434_missing_test_rows_{date_stamp}.txt"
    else:
        output_path = args.output

    print(f"Scanning root: {root_directory}")
    print(f"Date filter: {target_date.isoformat()}")
    print(f"Date source: {args.date_source}")
    print("File filter:", "all files" if args.all_extensions else ".txt files only")
    print()

    candidate_files = collect_target_date_files(
        root_directory=root_directory,
        target_date=target_date,
        all_extensions=args.all_extensions,
        date_source=args.date_source,
    )

    print()
    print(f"Candidate files found: {len(candidate_files)}")

    suspect_reports = find_suspect_reports(candidate_files)

    write_results(output_path, suspect_reports)

    print()
    print("Suspect reports missing detailed test rows:")
    print("-------------------------------------------")

    if suspect_reports:
        for report_path in suspect_reports:
            print(report_path)
    else:
        print("None found.")

    print()
    print(f"Total suspect reports: {len(suspect_reports)}")
    print(f"Output written to: {output_path}")

    return 1 if suspect_reports else 0


if __name__ == "__main__":
    raise SystemExit(main())
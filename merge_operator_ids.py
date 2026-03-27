#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge operator ID mapping INI files into one deduplicated output file.

This program reads one or more INI files containing an [OperatorID] section
that maps operator IDs to operator names, merges the mappings, removes exact
duplicates, sorts the final entries by operator ID, and writes a single merged
INI file.

Expected input format example:
    ; Maps operator ID to operator name

    [OperatorID]
    1234567=Donald Duck
    1111111=Mickey Mouse

Behavior:
- Entries are merged from all input files.
- Duplicate entries with the same operator ID and same name are accepted.
- Conflicting entries with the same operator ID but different names cause an
  error by default.
- Output is sorted by operator ID.
- Comments from source files are not preserved.

Example:
    python merge_operator_ids.py \
        --input operators_a.ini operators_b.ini operators_c.ini \
        --output merged_operator_ids.ini
"""

from __future__ import annotations

import argparse
import configparser
import sys
from pathlib import Path


SECTION_NAME = "OperatorID"


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Merge one or more operator ID mapping INI files into a single "
            "deduplicated, sorted INI file."
        ),
        epilog=(
            "Input files must contain an [OperatorID] section with entries in "
            "the form OPERATOR_ID=Operator Name.\n\n"
            "Example:\n"
            "  python merge_operator_ids.py "
            "--input a.ini b.ini c.ini "
            "--output merged.ini"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--input",
        nargs="+",
        type=Path,
        required=True,
        help=(
            "One or more input INI files to merge. "
            "Each file must contain an [OperatorID] section."
        ),
    )

    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Path to the output merged INI file.",
    )

    parser.add_argument(
        "--encoding",
        default="utf-8",
        help=(
            "Text encoding to use when reading and writing files. "
            "Default: %(default)s"
        ),
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow overwriting the output file if it already exists.",
    )

    return parser.parse_args()


def load_operator_mappings(
    input_paths: list[Path],
    encoding: str,
) -> dict[str, str]:
    """Load and merge operator mappings from multiple INI files.

    Args:
        input_paths: Paths to input INI files.
        encoding: File encoding used to read the INI files.

    Returns:
        A dictionary mapping operator IDs to operator names.

    Raises:
        FileNotFoundError: If an input file does not exist.
        ValueError: If a file is invalid, missing the required section, or
            contains conflicting names for the same operator ID.
    """
    merged_mappings: dict[str, str] = {}

    for input_path in input_paths:
        if not input_path.is_file():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        config_parser = configparser.ConfigParser(interpolation=None)
        config_parser.optionxform = str  # Preserve operator ID key text as-is.

        try:
            with input_path.open("r", encoding=encoding) as input_file:
                config_parser.read_file(input_file)
        except configparser.Error as exc:
            raise ValueError(
                f"Failed to parse INI file '{input_path}': {exc}"
            ) from exc

        if SECTION_NAME not in config_parser:
            raise ValueError(
                f"Input file '{input_path}' does not contain the "
                f"required [{SECTION_NAME}] section."
            )

        for operator_id, operator_name in config_parser[SECTION_NAME].items():
            normalized_operator_id = operator_id.strip()
            normalized_operator_name = operator_name.strip()

            if not normalized_operator_id:
                raise ValueError(
                    f"File '{input_path}' contains a blank operator ID."
                )

            if normalized_operator_id in merged_mappings:
                existing_name = merged_mappings[normalized_operator_id]
                if existing_name != normalized_operator_name:
                    raise ValueError(
                        "Conflicting operator mapping found for ID "
                        f"'{normalized_operator_id}': "
                        f"'{existing_name}' vs '{normalized_operator_name}' "
                        f"in file '{input_path}'."
                    )
            else:
                merged_mappings[normalized_operator_id] = normalized_operator_name

    return merged_mappings


def sort_operator_mappings(
    operator_mappings: dict[str, str],
) -> list[tuple[str, str]]:
    """Sort operator mappings by operator ID.

    Numeric operator IDs are sorted numerically when possible. Non-numeric IDs
    are sorted after numeric IDs using normal string ordering.

    Args:
        operator_mappings: Dictionary of operator ID to operator name.

    Returns:
        A sorted list of (operator_id, operator_name) tuples.
    """

    def sort_key(operator_entry: tuple[str, str]) -> tuple[int, int | str]:
        operator_id = operator_entry[0]
        if operator_id.isdigit():
            return (0, int(operator_id))
        return (1, operator_id)

    return sorted(operator_mappings.items(), key=sort_key)


def write_operator_mappings(
    output_path: Path,
    sorted_operator_mappings: list[tuple[str, str]],
    encoding: str,
    overwrite: bool,
) -> None:
    """Write merged operator mappings to an output INI file.

    Args:
        output_path: Destination INI file path.
        sorted_operator_mappings: Sorted operator ID and name pairs.
        encoding: File encoding used to write the INI file.
        overwrite: Whether an existing output file may be overwritten.

    Raises:
        FileExistsError: If the output file exists and overwrite is False.
    """
    if output_path.exists() and not overwrite:
        raise FileExistsError(
            f"Output file already exists: {output_path}. "
            "Use --overwrite to replace it."
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding=encoding, newline="\n") as output_file:
        output_file.write("; Maps operator ID to operator name\n\n")
        output_file.write(f"[{SECTION_NAME}]\n")
        for operator_id, operator_name in sorted_operator_mappings:
            output_file.write(f"{operator_id}={operator_name}\n")


def main() -> int:
    """Run the program.

    Returns:
        Process exit code. Returns 0 on success, non-zero on failure.
    """
    arguments = parse_arguments()

    try:
        operator_mappings = load_operator_mappings(
            input_paths=arguments.input,
            encoding=arguments.encoding,
        )
        sorted_operator_mappings = sort_operator_mappings(operator_mappings)
        write_operator_mappings(
            output_path=arguments.output,
            sorted_operator_mappings=sorted_operator_mappings,
            encoding=arguments.encoding,
            overwrite=arguments.overwrite,
        )
    except (FileNotFoundError, FileExistsError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(
        f"Merged {len(arguments.input)} file(s) into '{arguments.output}' "
        f"with {len(sorted_operator_mappings)} unique operator ID mapping(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
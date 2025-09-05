#!/usr/bin/env python3
"""
Recursively extract UNIQUE 7-digit Operator IDs from *.txt files and write them
(sorted) to unique_operator_id.txt. Shows tqdm progress during file enumeration
and during scanning.

Usage:
    pip install tqdm
    python extract_operator_ids.py /path/to/dir
    python extract_operator_ids.py . -o out.txt
    python extract_operator_ids.py . --no-progress
"""

from __future__ import annotations
import argparse
import sys
from pathlib import Path
import re

try:
    from tqdm import tqdm
except ImportError:
    print("Error: tqdm is required. Install it with: pip install tqdm", file=sys.stderr)
    sys.exit(1)

# Case-insensitive; allows extra spaces and :, =, or - as the delimiter.
# Anchored to the start of a line (with optional leading spaces).
OP_ID_PATTERN = re.compile(
    r"^\s*Operator\s*ID\s*[:=\-]\s*(\d{7})\b",
    re.IGNORECASE | re.MULTILINE,
)

def read_text_safely(path: Path) -> str:
    """
    Try several common encodings to robustly read text files (Windows/Linux exports).
    Falls back to ignoring undecodable bytes if needed.
    """
    for enc in ("utf-8", "utf-16", "cp1252", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeError:
            continue
        except OSError:
            raise
    return path.read_text(encoding="utf-8", errors="ignore")

def enumerate_txt_files(root: Path, show_progress: bool) -> list[Path]:
    """
    Enumerate *.txt files under root with visible progress feedback.
    Returns a list (used to know the total for the subsequent scan bar).
    """
    if not show_progress:
        return root.rglob("*.txt")

    files: list[Path] = []
    # Unknown total during discovery; show a live counter and rate.
    with tqdm(desc="Enumerating *.txt files", unit="file", dynamic_ncols=True) as pbar:
        for txt in root.rglob("*.txt"):
            files.append(txt)
            pbar.update(1)
            # Periodically surface a count in the postfix without spamming the terminal.
            if len(files) % 5000 == 0:
                pbar.set_postfix_str(f"found={len(files):,}")

    tqdm.write(f"Enumeration complete. Found {len(files):,} *.txt file(s).")
    return files

def collect_operator_ids(files: list[Path], show_progress: bool) -> set[str]:
    ids: set[str] = set()
    iterator = files
    if show_progress:
        iterator = tqdm(files, desc="Scanning", unit="file", dynamic_ncols=True, total=len(files))

    for txt_path in iterator:
        try:
            text = read_text_safely(txt_path)
        except OSError as e:
            # Keep the progress bar intact when logging warnings
            tqdm.write(f"Warning: could not read {txt_path}: {e}")
            continue

        for m in OP_ID_PATTERN.finditer(text):
            ids.add(m.group(1))

    return ids

def write_ids(ids: set[str], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        for op_id in sorted(ids):  # fixed width => lexicographic == numeric
            f.write(op_id + "\n")

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Recursively extract UNIQUE 7-digit Operator IDs from *.txt files."
    )
    p.add_argument("directory", type=Path, help="Root directory to scan.")
    p.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("unique_operator_id.txt"),
        help="Output file path (default: unique_operator_id.txt).",
    )
    p.add_argument(
        "--no-progress",
        action="store_true",
        help="Disable tqdm progress bars.",
    )
    return p.parse_args(argv)

def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root: Path = args.directory

    if not root.exists() or not root.is_dir():
        print(f"Error: '{root}' is not a directory.", file=sys.stderr)
        return 2

    files = enumerate_txt_files(root, show_progress=not args.no_progress)
    if not files:
        print("No *.txt files found. Nothing to do.")
        return 0

    ids = collect_operator_ids(files, show_progress=not args.no_progress)
    write_ids(ids, args.output)

    print(f"Found {len(ids)} unique Operator ID(s). Wrote: {args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

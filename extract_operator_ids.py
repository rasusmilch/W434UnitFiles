#!/usr/bin/env python3
"""
Recursively extract UNIQUE 7-digit Operator IDs from *.txt files and write them
(sorted) to unique_operator_id.txt. Uses tqdm for progress bars and a thread pool
for concurrent extraction.

Usage:
    pip install tqdm
    python extract_operator_ids.py /path/to/dir
    python extract_operator_ids.py . -o out.txt
    python extract_operator_ids.py . --no-progress
    python extract_operator_ids.py . --workers 16
"""

from __future__ import annotations
import argparse
import sys
from pathlib import Path
import re
import os
from concurrent.futures import ThreadPoolExecutor

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
    Returns a materialized list so we know the total for scanning.
    Preserves traversal order (no sorting).
    """
    if not show_progress:
        return list(root.rglob("*.txt"))

    files: list[Path] = []
    with tqdm(desc="Enumerating *.txt files", unit="file", dynamic_ncols=True) as pbar:
        for txt in root.rglob("*.txt"):
            files.append(txt)
            pbar.update(1)
            if len(files) % 5000 == 0:
                pbar.set_postfix_str(f"found={len(files):,}")

    tqdm.write(f"Enumeration complete. Found {len(files):,} *.txt file(s).")
    return files

def extract_ids_from_file(path: Path) -> set[str]:
    """
    Worker: read a single file and return a set of IDs found.
    Exceptions are handled here so the caller can iterate safely.
    """
    try:
        text = read_text_safely(path)
    except OSError as e:
        # Use tqdm.write to avoid breaking progress bars (even if bars are disabled, it's harmless).
        tqdm.write(f"Warning: could not read {path}: {e}")
        return set()

    return {m.group(1) for m in OP_ID_PATTERN.finditer(text)}

def collect_operator_ids_threaded(files: list[Path], show_progress: bool, workers: int) -> set[str]:
    """
    Run a thread pool over files. Uses executor.map with chunksize=1 so we can
    stream results and update the progress bar smoothly without enqueuing
    hundreds of thousands of futures at once.
    """
    unique_ids: set[str] = set()

    # Defensive default: plenty for I/O-bound work without going silly.
    if workers <= 0:
        workers = 4

    with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="opid") as executor:
        mapped = executor.map(extract_ids_from_file, files, chunksize=1)
        if show_progress:
            mapped = tqdm(mapped, total=len(files), desc="Scanning", unit="file", dynamic_ncols=True)

        for id_set in mapped:
            # Merge incrementally; set.update is efficient.
            if id_set:
                unique_ids.update(id_set)

    return unique_ids

def write_ids(ids: set[str], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        for op_id in sorted(ids):  # sort IDs only
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
    p.add_argument(
        "--workers",
        type=int,
        default=0,
        help="Number of worker threads (default: 4 for network bound workloads).",
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

    ids = collect_operator_ids_threaded(
        files=files,
        show_progress=not args.no_progress,
        workers=args.workers,
    )
    write_ids(ids, args.output)

    print(f"Found {len(ids)} unique Operator ID(s). Wrote: {args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

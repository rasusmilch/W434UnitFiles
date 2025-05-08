import shutil
import sys
import argparse
from pathlib import Path
from tqdm import tqdm
from loguru import logger
from utilities.log_util import *

TESTSTARTPROGRAM = r'.\TestStartPrograms\NortechTestStartProgram.teststart'
TESTENDPROGRAM = r'.\TestEndPrograms\ConsolidatedArchiveReport.testend'

test_start_replace = []

test_end_replace = ['ABILITECH ArchiveReport', 'AERIN ArchiveReport', r'\ArchiveReport.testend', 
                    'ASI DATAMYTE ArchiveReport', 'BIBLIOTHECA ArchiveReport', 'CLS ArchiveReport',
                    'CSI ArchiveReport', 'DefaultTestEndProgram', 'Devicix ArchiveReport', 
                    'DRS ArchiveReport', 'FSI ArchiveReport', 'GE COILS ArchiveReport', 
                    'GE Trans ArchiveReport', 'GEHC ArchiveReport', 'GEHC-FLEX ArchiveReport',
                    'Halyard AchiveReport', 'INTERCON ArchiveReport', 'KLUNE ArchiveReport', 
                    'Milaca ArchiveReport', 'MINERVA ArchiveReport', 'MONTERIS ArchiveReport',
                    'MR InstrumentsArchiveReport', 'NATUS ArchiveReport', 'NeocoilArchiveReport',
                    'NEOVIEW ArchiveReport', 'NEXTHERA ArchiveReport', 'NNT ArchiveReport',
                    'NXTHERA ArchiveReport', 'PHY ArchiveReport', 'QUEST ArchiveReport',
                    'ROSEMOUNT ArchiveReport', 'SANUWAVE ArchiveReport', 'SOTERA ArchiveReport',
                    'TerumoArchiveReport', 'TEST LAB ArchiveReport', 'TSI ArchiveReport',
                    'UroVal ArchiveReport', 'VARIAN ArchiveReport', 'ZOLL ArchiveReport']

def update_project(file_path, safe):
    file_path = Path(file_path)

    with open(file_path, 'r') as file:
        file_content = file.readlines()

    new_lines = []

    for line in file_content:
        original_line = line.strip()
        updated_line = original_line
        line_upper = original_line.upper()

        if line_upper.startswith("TESTSTARTPROGRAM="):
            if line_upper == "TESTSTARTPROGRAM=":
                updated_line = f"TestStartProgram={TESTSTARTPROGRAM}"

        elif line_upper.startswith("TESTENDPROGRAM="):
            for program in test_end_replace:
                if program.upper() in line_upper:
                    updated_line = f"TestEndProgram={TESTENDPROGRAM}"
                    break

        if safe:
            if original_line != updated_line:
                logger.info(f"[SAFE MODE] Would replace in {file_path}:\n     {original_line}\n  -> {updated_line}")
        else:
            new_lines.append(f"{updated_line}\n")

    if not safe:
        # Backup original file
        backup_path = file_path.with_suffix(file_path.suffix + '.bak')
        shutil.copyfile(file_path, backup_path)
        logger.info(f"Backup created at {backup_path}")

        # Write updated content to the original file
        with file_path.open('w') as file:
            file.writelines(new_lines)
        logger.info(f"Updated file written to {file_path}")

def process_all_project_files(project_files, safe, pbar):
    for path in project_files:
        update_project(path, safe)
        if pbar is not None:
            pbar.update(1)

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        """
        Override the default `error` method to suppress duplicate output.
        Prints the help message and the custom error message, then exits.
        """
        sys.stderr.write(f"error: {message}\n\n")
        self.print_help()
        sys.exit(2)

def crawl_directory(directory, safe):
    # Use rglob to gather all .project files
    project_files = list(Path(directory).rglob('*.project'))
    total_files = len(project_files)

    logger.info(f"Found {total_files} project files matching")

    if safe:
        # No tqdm if in safe mode
        process_all_project_files(project_files, safe, pbar=None)
    else:
        # Use tqdm for progress tracking
        with tqdm(
            total=total_files,
            desc="Processing files",
            unit="file",
            dynamic_ncols=True,
            disable=not sys.stdout.isatty()
        ) as pbar:
            process_all_project_files(project_files, safe, pbar)

        

def main():
    # Set up argument parser
    configure_logger(__file__)

    parser = CustomArgumentParser(
        description="Update project files for new test start and end programs"
    )

    parser.add_argument("-d", "--dir", type=str, required=True, help="Crawl directory")
    parser.add_argument("-s", "--safe", default=False, action="store_true", help="Do not modify files")

    # Parse arguments
    args = parser.parse_args()

    if args.dir:
        crawl_directory(args.dir, args.safe)

if __name__ == "__main__":
    main()

"""Generates an AOC skeleton code for a day"""

import os
import argparse

YEAR_RANGE = range(2015, 2025)
DAY_RANGE  = range(1, 26)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def make_parser() -> argparse.ArgumentParser:
    """Simple argument parser.
    """
    parser = argparse.ArgumentParser(description="Generates an AOC skeleton code for a day",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("year", type=int, help="Year to generate day from", choices=YEAR_RANGE, default=None)
    parser.add_argument("day",  type=int, help="Day to generate",           choices=DAY_RANGE,  default=None)
    return parser.parse_args()


def validate_args(year : int, day : int) -> None :
    """Validates input arguments

    Parameters
    ----------
    year : int
        Year to generate
    day : int
        Day to generate

    Raises
    ------
    ValueError
        Year or day not in supported range
    """
    if not year in YEAR_RANGE:
        raise ValueError("No advent of code for this year")
    if not day in DAY_RANGE:
        raise ValueError("This day is not in the Advent of Code")


def create_script(directory : str, day : int, year : int):
    """Create the script for an advent day

    Parameters
    ----------
    directory : str
        Directory to create the script in
    day : int
    year : int
    """
    with open(os.path.join(directory, f"day{day}.py"), "wt", encoding='utf-8') as f:
        f.write(f"\"\"\"Code for day {day} of AOC{year}\"\"\"\n\n")
        f.write("import log\n\n")
        f.write("def main_first_part(filename : str):\n")
        f.write("    \"\"\"First part of the day\n")
        f.write("    Parameters\n")
        f.write("    ----------\n")
        f.write("    filename : str\n")
        f.write("        Input file\n")
        f.write("    \"\"\"\n")
        f.write("    log.log.info(\"Executing part 1\")\n")
        f.write("    with open(filename, \"rt\", encoding=\'utf-8\') as input_data:\n")
        f.write("        output = 0\n")
        f.write(f"        log.log.info(\"Day1 result for %s is: %d\", filename, output)\n")
        f.write("\n")
        f.write("def main_second_part(filename : str):\n")
        f.write("    \"\"\"Second part of the day\n")
        f.write("    Parameters\n")
        f.write("    ----------\n")
        f.write("    filename : str\n")
        f.write("        Input file\n")
        f.write("    \"\"\"\n")
        f.write("    log.log.info(\"Executing part 2\")\n")
        f.write("    with open(filename, \"rt\", encoding=\'utf-8\') as input_data:\n")
        f.write("        output = 0\n")
        f.write(f"        log.log.info(\"Day1 result for %s is: %d\", filename, output)\n")
        f.write("\n")
        f.write("def main(filename : str, part: int):\n")
        f.write("    \"\"\"Main function of the module\n")
        f.write("    Parameters\n")
        f.write("    ----------\n")
        f.write("    filename : str\n")
        f.write("        Input file\n")
        f.write("    part : int\n")
        f.write("        Part of the day to run\n")
        f.write("    \"\"\"\n")
        f.write(f"    log.log.info(f\"Executing Day{day} for %s\", filename)\n")
        f.write("    match part:\n")
        f.write("        case 1:\n")
        f.write("            main_first_part(filename)\n")
        f.write("        case 2:\n")
        f.write("            main_second_part(filename)\n")


def input_placeholders(directory : str, day : int):
    """Creates placeholders for input files

    Parameters
    ----------
    directory : str
        Directory of the AOC year
    day : int
        Day to generate inputs for
    """
    in_dir = os.path.join(directory, "inputs")
    os.makedirs(in_dir, exist_ok=True)

    with open(os.path.join(in_dir, f"day{day}_input.txt"), "w", encoding='utf-8') as _:
        pass

    with open(os.path.join(in_dir, f"day{day}_sample1.txt"), "w", encoding='utf-8') as _:
        pass
    with open(os.path.join(in_dir, f"day{day}_sample2.txt"), "w", encoding='utf-8') as _:
        pass


def main(year : int, day : int):
    """Main function of the module that generates and AOC day

    Parameters
    ----------
    year : int
    day : int
    """
    validate_args(year, day)

    directory = os.path.join(SCRIPT_DIR, str(year))
    os.makedirs(directory, exist_ok=True)

    create_script(directory, day, year)
    input_placeholders(directory, day)


if __name__ == "__main__":
    args = make_parser()
    main(args.year, args.day)

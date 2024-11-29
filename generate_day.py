import os
import requests
import argparse
import tqdm

YEAR_RANGE = range(2015, 2025)
DAY_RANGE  = range(1, 26)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def make_parser() -> argparse.ArgumentParser:
    """Simple argument parser.
    """
    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("year", type=int, help="Year to generate day from", choices=YEAR_RANGE, default=None)
    parser.add_argument("day",  type=int, help="Day to generate",           choices=DAY_RANGE,  default=None)
    args = parser.parse_args()
    return args


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
    """
    if not year in YEAR_RANGE:
        raise ValueError("No advent of code for this year")
    if not day in DAY_RANGE:
        raise ValueError("This day is not in the Advent of Code")


def create_script(directory : str, day : int):
    with open(os.path.join(directory, f"day{day}.py"), "w") as f:
        f.write(f"import log\n\n")
        f.write(f"def main_first_part(filename : str):\n")
        f.write(f"    log.log.info(\"Executing part 1\")\n")
        f.write(f"    with open(filename, \"rt\") as input_data:\n")
        f.write(f"        pass\n")
        f.write(f"\n")
        f.write(f"def main_second_part(filename : str):\n")
        f.write(f"    log.log.info(\"Executing part 2\")\n")
        f.write(f"    with open(filename, \"rt\") as input_data:\n")
        f.write(f"        pass\n")
        f.write(f"\n")
        f.write(f"def main(filename : str, part: int):\n")
        f.write(f"    log.log.info(f\"Executing Day{day} for {{filename}}\")\n")
        f.write(f"    match part:\n")
        f.write(f"        case 1:\n")
        f.write(f"            main_first_part(filename)\n")
        f.write(f"        case 2:\n")
        f.write(f"            main_second_part(filename)\n")


def input_placeholders(directory : str, day : int):
    in_dir = os.path.join(directory, "inputs")
    os.makedirs(in_dir, exist_ok=True)

    with open(os.path.join(in_dir, f"day{day}_input.txt"), "w") as _:
        pass

    with open(os.path.join(in_dir, f"day{day}_sample1.txt"), "w") as _:
        pass
    with open(os.path.join(in_dir, f"day{day}_sample2.txt"), "w") as _:
        pass


def main(year : int, day : int):
    validate_args(year, day)

    directory = os.path.join(SCRIPT_DIR, str(year))
    os.makedirs(directory, exist_ok=True)

    create_script(directory, day)
    input_placeholders(directory, day)


if __name__ == "__main__":
    args = make_parser()
    main(args.year, args.day)
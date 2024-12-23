import log
import os
import argparse

import day1
import day2
import day3

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def make_parser() -> argparse.ArgumentParser:
    """Simple argument parser.
    """
    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("day",  type=int, help="Advent day", choices=range(1, 26))
    parser.add_argument("part", type=int, help="Which part of the task should I run?", choices=[1, 2], default=1)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    log.log.info("Hello, Adina")

    args = make_parser()
    inputs_dir = os.path.join(SCRIPT_DIR, "inputs")
    files = [os.path.join(inputs_dir, f) for f in os.listdir(inputs_dir) if f"day{args.day}" in f if f.endswith(".txt")]
    # Filter samples, as input may not be supported
    files = [f for f in files if "input" in os.path.basename(f) or f"sample{args.part}" in os.path.basename(f)]

    fn = None

    match args.day:
        case 1:
            fn = day1.main
        case 2:
            fn = day2.main
        case 3:
            fn = day3.main

    for f in files:
        fn(f, args.part)

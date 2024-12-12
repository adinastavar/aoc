"""The main module for AOC2024"""
import os
import argparse

import log
import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day11
import day12

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def make_parser() -> argparse.ArgumentParser:
    """Simple argument parser.
    """
    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("day",  type=int, help="Advent day", choices=range(1, 26))
    parser.add_argument("part", type=int, help="Which part of the task should I run?", choices=[1, 2], default=1)
    return parser.parse_args()

if __name__ == "__main__":
    log.log.info("Hello, Adina")

    args = make_parser()
    inputs_dir = os.path.join(SCRIPT_DIR, "inputs")
    files = [os.path.join(inputs_dir, f) for f in os.listdir(inputs_dir) \
             if f"day{args.day}" in f if f.endswith(".txt")]
    # Filter samples, as input may not be supported
    files = [f for f in files
            #  if "input" in os.path.basename(f) or f"sample{args.part}" in os.path.basename(f)]
             if f"sample{args.part}" in os.path.basename(f)]

    fn = None

    match args.day:
        case 1:
            fn = day1.main
        case 2:
            fn = day2.main
        case 3:
            fn = day3.main
        case 4:
            fn = day4.main
        case 5:
            fn = day5.main
        case 6:
            fn = day6.main
        case 7:
            fn = day7.main
        case 8:
            fn = day8.main
        case 9:
            fn = day9.main
        case 10:
            fn = day10.main
        case 11:
            fn = day11.main
        case 12:
            fn = day12.main

    for f in files:
        fn(f, args.part)

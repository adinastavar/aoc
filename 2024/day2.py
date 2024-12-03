"""Code for day 2 of AOC2024"""
from typing import List

import log

def is_safe(levels : List[int]) -> bool:
    """Checks if a list of levels is safe

    Parameters
    ----------
    levels : List[int]
        List of levels

    Returns
    -------
    bool
    """
    safe = True

    ascending = sorted(levels, reverse=False)
    descending = sorted(levels, reverse=True)

    if levels != ascending and levels != descending:
        safe = False
    else:
        for i in range(0, len(levels) - 1):
            diff = abs(levels[i] - levels[i+1])
            if diff == 0 or diff > 3:
                safe = False
                break
    return safe

def main_first_part(filename : str):
    """First part of the day
    Parameters
    ----------
    filename : str
        Input file
    """
    log.log.info("Executing part 1")
    with open(filename, "rt", encoding='utf-8') as input_data:
        output = 0

        for report in input_data:
            levels = [int(d) for d in report.strip().split()]
            if is_safe(levels):
                output += 1

        log.log.info("Day1 result for %s is: %d", filename, output)

def main_second_part(filename : str):
    """Second part of the day
    Parameters
    ----------
    filename : str
        Input file
    """
    log.log.info("Executing part 2")
    with open(filename, "rt", encoding='utf-8') as input_data:
        output = 0
        for report in input_data:
            safe = False
            levels = [int(d) for d in report.strip().split()]

            if is_safe(levels):
                safe = True
            elif is_safe(levels[1:]):
                safe = True
            elif is_safe(levels[:len(levels) - 1]):
                safe = True
            else:
                for i in range(1, len(levels) - 1):
                    if is_safe(levels[0:i] + levels[i+1: len(levels)]):
                        safe = True
                        break

            if safe:
                output += 1

        log.log.info("Day1 result for %s is: %d", filename, output)

def main(filename : str, part: int):
    """Main function of the module
    Parameters
    ----------
    filename : str
        Input file
    part : int
        Part of the day to run
    """
    log.log.info(f"Executing Day2 for {filename}")
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

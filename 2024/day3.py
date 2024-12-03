"""Code for day 3 of AOC2024"""
import re

import log

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

        file_content = input_data.read()
        matches = re.finditer(r"mul\((\d+)\,(\d+)\)", file_content)
        for m in matches:
            output += int(m.group(1)) * int(m.group(2))

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

        file_content = input_data.read()
        file_content = ''.join(file_content.split())

        actions = file_content.split("don't()")
        for a in actions:
            match = re.search(r"do\(\)", a)
            if match:
                start = match.span()[1]
                operations = re.finditer(r"mul\((\d+)\,(\d+)\)", a[start:])
                for m in operations:
                    output += int(m.group(1)) * int(m.group(2))

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
    log.log.info("Executing Day3 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

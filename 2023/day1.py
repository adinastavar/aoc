"""Code for day 1 of AOC2023"""

import re
import log

number_string_map = {
    "one"   : 1,
    "two"   : 2,
    "three" : 3,
    "four"  : 4,
    "five"  : 5,
    "six"   : 6,
    "seven" : 7,
    "eight" : 8,
    "nine"  : 9
}
number_string_map.update({str(d) : d for d in range(10)})


def main_first_part(filename : str):
    """First part of the day

    Parameters
    ----------
    filename : str
        Input file
    """
    log.log.info("Executing part 1")
    output = 0
    with open(filename, "rt", encoding='utf-8') as input_data:
        for line in input_data:
            integers = [d for d in line if d.isdigit()]
            number = int(integers[0]) * 10 + int(integers[-1])
            output += number
    log.log.info("Day1 result is: %d", output)


def main_second_part(filename : str):
    """Second part of the day

    Parameters
    ----------
    filename : str
        Input file
    """
    log.log.info("Executing part 2")

    output = 0
    with open(filename, "rt", encoding='utf-8') as input_data:
        for line in input_data:
            line = line.strip()
            first_index = len(line)
            last_index = -1
            first_number = None
            last_number = None
            for token in number_string_map:
                indices = [m.start() for m in re.finditer(token, line)]
                if len(indices):
                    if indices[0] < first_index:
                        first_index = indices[0]
                        first_number = number_string_map[token]
                    if indices[-1] > last_index:
                        last_index = indices[-1]
                        last_number = number_string_map[token]
            output += 10 * first_number + last_number

    log.log.info("Day1 result is: %d", output)

def main(filename : str, part: int):
    """Main module for AOC2023 day 1

    Parameters
    ----------
    filename : str
        Input file
    part : int
        Part of day to run
    """
    log.log.info("Executing Day1 for %s", filename)

    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

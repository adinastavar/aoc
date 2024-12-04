"""Code for day 4 of AOC2024"""

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
        input_data = input_data.readlines()
        for y, line in enumerate(input_data):
            for x, c in enumerate(line):
                if c == 'X':
                    # horizontal ->
                    if line[x+1:].startswith('MAS'):
                        output += 1
                    # horizontal <-
                    if line[:x].endswith('SAM'):
                        output += 1
                    if y >= 3:
                        # vertical ^
                        if input_data[y-1][x] == 'M' and input_data[y-2][x] == 'A' and input_data[y-3][x] == 'S':
                            output += 1
                        # upward diagonal \
                        if input_data[y-1][x -1] == 'M' and input_data[y-2][x - 2] == 'A' and input_data[y-3][x -3 ] == 'S':
                            output += 1
                        # upward diagonal /
                        if input_data[y-1][x +1] == 'M' and input_data[y-2][x + 2] == 'A' and input_data[y-3][x +3 ] == 'S':
                            output += 1

                    if y <= len(input_data) - 4:
                        # vertical V
                        if input_data[y+1][x] == 'M' and input_data[y+2][x] == 'A' and input_data[y+3][x] == 'S':
                            output += 1
                        # downward diagonal /
                        if input_data[y+1][x -1] == 'M' and input_data[y+2][x - 2] == 'A' and input_data[y+3][x -3 ] == 'S':
                            output += 1
                        # downward diagonal \
                        if input_data[y+1][x +1] == 'M' and input_data[y+2][x + 2] == 'A' and input_data[y+3][x +3 ] == 'S':
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
        input_data = input_data.readlines()

        to_find = set(['MAS', 'SAM'])
        for y, line in enumerate(input_data):
            if y == 0 or y == len(input_data) - 1:
                continue
            for x, c in enumerate(line):
                if x == 0 or x == len(line) - 1:
                    continue
                if c == 'A':
                    diagonal1 = input_data[y-1][x-1] + c + input_data[y+1][x+1]
                    diagonal2 = input_data[y-1][x+1] + c + input_data[y+1][x-1]
                    if diagonal1 in to_find and diagonal2 in to_find:
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
    log.log.info(f"Executing Day4 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

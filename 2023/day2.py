"""Code for day 2 of AOC2023"""
from functools import reduce
from operator import mul
from typing import List

import log

def get_balls(line : str) -> List[str]:
    """Returns the balls in a line

    Parameters
    ----------
    line : str
        Input line

    Returns
    -------
    List[str]
        Returns a list of balls from a game
    """
    # extract the `Game:` prefix
    game = line.split(":")[-1]
    game = game.replace(";", ",")
    game = game.split(",")
    game = [g.strip() for g in game]
    return game


def main_first_part(filename : str):
    """First part of the day

    Parameters
    ----------
    filename : str
        Input file
    """
    log.log.info("Executing part 1")

    with open(filename, "rt", encoding='utf-8') as input_data:
        MAX : dict = {
            'red'   : 12,
            'green' : 13,
            'blue'  : 14
        }
        output = 0

        for idx, line in enumerate(input_data):
            is_valid = True
            for s in get_balls(line):
                number, key = s.strip().split(" ")
                if int(number) > MAX[key]:
                    is_valid = False
                    break
            if is_valid:
                output += (idx + 1)

        log.log.info("Day2 result is: %d", output)


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

        for line in input_data:
            power = 1
            min_num_balls = {
                'red' : 0,
                'green' : 0,
                'blue' : 0
            }
            for s in get_balls(line):
                number, key = s.split(" ")
                number = int(number)
                if number > min_num_balls[key]:
                    min_num_balls[key] = number

            power = reduce(mul, min_num_balls.values())
            output += power

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
    log.log.info("Executing Day2 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

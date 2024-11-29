import log
from dataclasses import dataclass
from typing import List

@dataclass
class Part:
    number : int
    x : int
    y : int

    def __init__(self, number : int, x : int, y : int):
        self.number = number
        self.x      = x
        self.y      = y

@dataclass
class SpecialChar:
    x : int
    y : int

    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y

def main_first_part(filename : str):
    log.log.info("Executing part 1")
    with open(filename, "rt") as input_data:
        sum = 0

        parts : List[Part] = []
        special_chars : List[SpecialChar] = []

        # Extract parts and special characters

        # Check for parts



        log.log.info(f"Day3 result is: {sum}")

def main_second_part(filename : str):
    log.log.info("Executing part 2")
    with open(filename, "rt") as input_data:
        pass

def main(filename : str, part: int):
    log.log.info(f"Executing Day3 for {filename}")
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)


import re
from dataclasses import dataclass
from typing import List

import log

@dataclass
class Part:
    number : str
    x : int
    y : int

    def __init__(self, number : str, x : int, y : int):
        self.number = number
        self.x      = x
        self.y      = y
    def __str__(self):
        return f"({self.x}, {self.y}) {self.number}"

@dataclass
class SpecialChar:
    x : int
    y : int

    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

def main_first_part(filename : str):
    log.log.info("Executing part 1")
    with open(filename, "rt", encoding='utf-8') as input_data:
        output = 0

        parts         : List[Part]        = []
        # Grouping characters into lines for easier search
        special_chars : dict[List[SpecialChar]] = {}

        # Extract parts and special characters
        number_re       = re.compile(r"\d+")
        special_char_re = re.compile(r"[^\d\.]")

        # Check for parts and special chars
        for y, line in enumerate(input_data):
            special_chars[y] = []
            for m in number_re.finditer(line):
                parts.append(Part(m.group(), m.start(), y))
            for m in special_char_re.finditer(line):
                special_chars[y].append(SpecialChar(int(m.start()), y))

        for part in parts:
            left_bound  = part.x - 1
            right_bound = part.x + len(part.number)
            top_bound = part.y - 1
            lower_bound = part.y + 1
            print(part)

        print(special_chars)

        log.log.info(f"Day3 result is: {output}")

def main_second_part(filename : str):
    log.log.info("Executing part 2")
    with open(filename, "rt", encoding='utf-8') as input_data:
        pass

def main(filename : str, part: int):
    log.log.info(f"Executing Day3 for {filename}")
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

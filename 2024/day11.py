"""Code for day 11 of AOC2024"""

import os
import sys
from typing import Dict
from dataclasses import dataclass
from collections import OrderedDict

import log

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

cache : OrderedDict = {
    "0" : "1"
}

def change(arrangement):
    new_arrangement = []
    for stone in arrangement:
        if stone == "0":
            new_arrangement.append("1")
        elif len(stone) % 2 == 0:
            new_arrangement.append(stone[:len(stone)// 2])
            second_part = stone[len(stone)// 2 : ]
            if int(second_part) == 0:
                new_arrangement.append("0")
            else:
                new_arrangement.append(second_part.lstrip('0'))
        else:
            new_arrangement.append(str(2024 * int(stone)))

    return new_arrangement

@dataclass
class Replacement:
    index : int
    old : str
    new : str

def find(string, c):
    return [idx for idx, char in enumerate(string) if char == c]


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
        data = input_data.read()
        arrangement = data.strip().split()
        for _ in range(25):
            arrangement = change(arrangement)
        output = len(arrangement)
        log.log.info("Day1 result for %s is: %d", filename, output)

def main_second_part(filename : str):
    """Second part of the day
    Parameters
    ----------
    filename : str
        Input file
    """
    global cache

    log.log.info("Executing part 2")
    with open(filename, "rt", encoding='utf-8') as input_data:
        output = 0
        data = input_data.read()
        arrangement = data.strip().split()
        for stone in arrangement:
            stone_dict : Dict[str, int]= {
                stone : 1
            }
            for _ in range(75):
                new_stone_dict : Dict[str, int] = {}

                for word, count in stone_dict.items():
                    if word in cache:
                        new_stone_dict[cache[word]] = new_stone_dict.get(cache[word], 0) + count
                    else:
                        if len(word) % 2 == 0:
                            word1 = word[:len(word)// 2]
                            word2 = str(int(word[len(word)// 2 : ]))
                            new_stone_dict[word1] = new_stone_dict.get(word1, 0) + count
                            new_stone_dict[word2] = new_stone_dict.get(word2, 0) + count
                        else:
                            new_word = str(int(word) * 2024)
                            new_stone_dict[new_word] = new_stone_dict.get(new_word, 0) + count
                            cache[word] = new_word
                stone_dict = new_stone_dict

            for _, count in stone_dict.items():
                output += count

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
    log.log.info(f"Executing Day11 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

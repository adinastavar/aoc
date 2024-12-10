"""Code for day 10 of AOC2024"""

import os
import sys

import log
from dataclasses import dataclass, field
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import adventOfCode.utils

@dataclass(unsafe_hash=True)
class TrailSpot():
    x : int = field(hash=True)
    y : int = field(hash=True)
    height : int = field(hash=True)
    next_steps : List = field(hash=False)

def getEnds(spot: TrailSpot, possible_ends : List[TrailSpot]):
    if spot.height == 9:
        possible_ends.append(spot)
    elif not spot.next_steps:
        return
    else:
        for child in spot.next_steps:
            getEnds(child, possible_ends)

def computeNumPath(spot : TrailSpot):
    if spot.height == 9:
        return 1
    elif not spot.next_steps:
        return 0
    else:
        return 0 + sum([computeNumPath(child) for child in spot.next_steps])


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
        map_spots : List[TrailSpot] = []
        for y, line in enumerate(input_data):
            line = line.strip()
            for x, v in enumerate(line):
                map_spots.append(TrailSpot(x, y, int(v), []))

        for spot in map_spots:
            spot.next_steps += [s for s in map_spots
                                if s.height - spot.height == 1
                                if abs(s.x - spot.x) + abs(s.y - spot.y) == 1]

        trailheads : List[TrailSpot] = [spot for spot in map_spots if spot.height == 0]
        for spot in trailheads:
            # Compute score
            possible_ends = []
            getEnds(spot, possible_ends)
            output += len(set(possible_ends))

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
        map_spots : List[TrailSpot] = []
        for y, line in enumerate(input_data):
            line = line.strip()
            for x, v in enumerate(line):
                map_spots.append(TrailSpot(x, y, int(v), []))

        for spot in map_spots:
            spot.next_steps += [s for s in map_spots
                                if s.height - spot.height == 1
                                if abs(s.x - spot.x) + abs(s.y - spot.y) == 1]

        trailheads : List[TrailSpot] = [spot for spot in map_spots if spot.height == 0]
        for spot in trailheads:
            # Compute score
            output += computeNumPath(spot)
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
    log.log.info(f"Executing Day10 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

"""Code for day 12 of AOC2024"""

import os
import sys
from typing import List, Dict, Set
from dataclasses import dataclass, field
from collections import OrderedDict

import log

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import adventOfCode.utils

@dataclass(unsafe_hash=True)
class Point:
    x : int = field(hash=True, compare=True)
    y : int = field(hash=True, compare=True)
    value : str = field(hash=True, compare=True)
    neighbors : List = field(default_factory=list, hash=False)

def update_region(pt : Point, region : Set[Point]):
    if not pt in region:
        region.add(pt)
        for neighbor in pt.neighbors:
            update_region(neighbor, region)

def compute_sides(region : List[Point]):
    corners = 0

    return corners

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
        points : OrderedDict[str, List[Point]] = {}

        for y, line in enumerate(input_data):
            for x, c in enumerate(line.strip()):
                if not points.get(c, None):
                    points[c] = [Point(x, y, c)]
                else:
                    points[c].append(Point(x, y, c))

        for _, ptList in points.items():
            # Update neighbors
            for pt in ptList:
                pt.neighbors = [other_pt for other_pt in ptList
                                if not (other_pt.x == pt.x and other_pt.y == pt.y)
                                if abs(other_pt.x - pt.x) + abs(other_pt.y - pt.y) == 1]

        for _, ptList in points.items():
            key_regions = []
            for pt in ptList:
                pt_region = set()
                update_region(pt, pt_region)
                if pt_region != set() and pt_region not in key_regions:
                    key_regions.append(pt_region)
            for region in key_regions:
                area = len(region)
                perimeter = sum([4 - len(pt.neighbors) for pt in region])
                output += area * perimeter

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
        points : OrderedDict[str, List[Point]] = {}

        for y, line in enumerate(input_data):
            for x, c in enumerate(line.strip()):
                if not points.get(c, None):
                    points[c] = [Point(x, y, c)]
                else:
                    points[c].append(Point(x, y, c))

        for _, ptList in points.items():
            # Update neighbors
            for pt in ptList:
                pt.neighbors = [other_pt for other_pt in ptList
                                if not (other_pt.x == pt.x and other_pt.y == pt.y)
                                if abs(other_pt.x - pt.x) + abs(other_pt.y - pt.y) == 1]

        for key, ptList in points.items():
            # Compute regions
            key_regions = []
            for pt in ptList:
                pt_region = set()
                update_region(pt, pt_region)
                if pt_region != set() and pt_region not in key_regions:
                    key_regions.append(pt_region)
            for region in key_regions:
                area = len(region)
                sides = compute_sides(region)
                print(f"{key} - area {area} sides {sides}")
                output += area * sides
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
    log.log.info(f"Executing Day12 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

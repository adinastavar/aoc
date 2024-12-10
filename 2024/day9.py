"""Code for day 9 of AOC2024"""

import os
import sys
from dataclasses import dataclass
from typing import List

import log

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import adventOfCode.utils

@dataclass(order=True)
class File:
    start : int
    end : int
    value : str
    checked : bool

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
        in_layout = input_data.read().strip()
        out_layout = []
        idx = 0
        total_num_fileblocks = 0
        for itr, char in enumerate(in_layout):
            nums = int(char)
            if itr % 2 == 0:
                # File block
                out_layout += [str(idx)] * nums
                total_num_fileblocks += nums
                idx += 1
            else:
                # Free space
                out_layout += ["."] * nums

        end_pos = len(out_layout) - 1
        for itr in range(total_num_fileblocks):
            if out_layout[itr] == ".":
                while out_layout[end_pos] == "." and end_pos >= total_num_fileblocks:
                    end_pos -= 1
                out_layout[itr], out_layout[end_pos] = out_layout[end_pos], out_layout[itr]
                end_pos -= 1
            output += int(out_layout[itr]) * itr

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
        in_layout = input_data.read().strip()
        files : List[File] = []
        out_layout :str = ""
        idx = 0
        position = 0
        for itr, char in enumerate(in_layout):
            num = int(char)
            if itr % 2 == 0:
                # File block
                length = num * len(str(idx))
                files.append(File(position, position + length, num * str(idx), False))
                position += length
                idx += 1
            else:
                position += num
        out_layout = '.' * position

        # Move files
        idx = len(files) - 1
        while idx > 0:
            if not files[idx].checked:
                files[idx].checked = True
                length = files[idx].end - files[idx].start
                start_idx = 0
                while start_idx < idx:
                    if files[start_idx + 1].start - files[start_idx].end >= length:
                        files[idx].start = files[start_idx].end
                        files[idx].end   = files[idx].start + length
                        files = sorted(files)
                        break
                    else:
                        start_idx += 1
            else:
                idx -= 1

        # Construct layout
        for f in files:
            out_layout = out_layout[:f.start] + f.value + out_layout[f.end:]
        print(out_layout)

        # Counting
        for idx, c in enumerate(out_layout):
            if c != ".":
                output += idx * int(c)

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
    log.log.info(f"Executing Day9 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

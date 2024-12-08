"""Code for day 8 of AOC2024"""

import log
import itertools

def in_bounds(x, y, max_x, max_y):
    if 0 <= x < max_x and 0 <= y < max_y:
        return True
    else:
        return False

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
        map_dict = {}
        antinodes = []
        len_x = 0
        len_y = 0

        for y, line in enumerate(input_data):
            line = line.strip()
            if y == 0:
                len_x = len(line)
            for x, c in enumerate(line):
                if c != '.':
                    if not map_dict.get(c, None):
                        map_dict[c] = [(y, x)]
                    else:
                        map_dict[c].append((y, x))
            len_y += 1

        for _, positions in map_dict.items():
            if len(positions) == 1:
                continue
            pos_pairs = itertools.combinations(positions, 2)
            for p in pos_pairs:
                y1, x1 = p[0]
                y2, x2 = p[1]
                diff_y, diff_x = abs(y2 - y1), abs(x2 - x1)
                min_x = min(x2, x1)
                min_y = min(y1, y2)
                max_x = max(x2, x1)
                max_y = max(y1, y2)

                if x1 == max_x and y1 == max_y:
                    # point1 is bottom, right
                    antinodes.append((y1 + diff_y, x1 + diff_x))
                    antinodes.append((y2 - diff_y, x2 - diff_x))
                elif x1 == max_x and y1 == min_y:
                    # point1 is up, right
                    antinodes.append((y1 - diff_y, x1 + diff_x))
                    antinodes.append((y2 + diff_y, x2 - diff_x))
                elif x1 == min_x and y1 == min_y:
                    # point1 is top, left
                    antinodes.append((y1 - diff_y, x1 - diff_x))
                    antinodes.append((y2 + diff_y, x2 + diff_x))
                elif x1 == min_x and y1 == max_y:
                    # point1 is bottom, left
                    antinodes.append((y1 + diff_y, x1 - diff_x))
                    antinodes.append((y2 - diff_y, x2 + diff_x))

        antinodes = [a for a in antinodes if in_bounds(a[1], a[0], len_x, len_y)]
        output = len(set(antinodes))
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
        map_dict = {}
        antinodes = []
        len_x = 0
        len_y = 0

        for y, line in enumerate(input_data):
            line = line.strip()
            if y == 0:
                len_x = len(line)
            for x, c in enumerate(line):
                if c != '.':
                    if not map_dict.get(c, None):
                        map_dict[c] = [(y, x)]
                    else:
                        map_dict[c].append((y, x))
            len_y += 1

        for _, positions in map_dict.items():
            antinodes += positions
            if len(positions) == 1:
                continue
            pos_pairs = itertools.combinations(positions, 2)
            for p in pos_pairs:
                y1, x1 = p[0]
                y2, x2 = p[1]
                diff_y, diff_x = abs(y2 - y1), abs(x2 - x1)
                min_x = min(x2, x1)
                min_y = min(y1, y2)
                max_x = max(x2, x1)
                max_y = max(y1, y2)

                itx = 1
                if x1 == max_x and y1 == max_y:
                    # point1 is bottom, right
                    while(True):
                        add = 0
                        if in_bounds(x1 + diff_x * itx, y1 + diff_y * itx, len_x, len_y):
                            antinodes.append((y1 + diff_y * itx, x1 + diff_x * itx))
                            add += 1
                        if in_bounds(x2 - diff_x * itx, y2 - diff_y * itx, len_x, len_y):
                            antinodes.append((y2 - diff_y * itx, x2 - diff_x * itx))
                            add += 1
                        if not add:
                            break
                        else:
                            itx += 1
                elif x1 == max_x and y1 == min_y:
                    # point1 is up, right
                    while(True):
                        add = 0
                        if in_bounds(x1 + diff_x * itx, y1 - diff_y * itx, len_x, len_y):
                            antinodes.append((y1 - diff_y * itx, x1 + diff_x * itx))
                            add += 1
                        if in_bounds(x2 - diff_x * itx, y2 + diff_y * itx, len_x, len_y):
                            antinodes.append((y2 + diff_y * itx, x2 - diff_x * itx))
                            add += 1
                        if not add:
                            break
                        else:
                            itx += 1
                elif x1 == min_x and y1 == min_y:
                    # point1 is top, left
                    while(True):
                        add = 0
                        if in_bounds(x1 - diff_x * itx, y1 - diff_y * itx, len_x, len_y):
                            antinodes.append((y1 - diff_y * itx, x1 - diff_x * itx))
                            add += 1
                        if in_bounds(x2 + diff_x * itx, y2 + diff_y * itx, len_x, len_y):
                            antinodes.append((y2 + diff_y * itx, x2 + diff_x * itx))
                            add += 1
                        if not add:
                            break
                        else:
                            itx += 1
                elif x1 == min_x and y1 == max_y:
                    # point1 is bottom, left
                    antinodes.append((y1 + diff_y, x1 - diff_x))
                    antinodes.append((y2 - diff_y, x2 + diff_x))
                    while(True):
                        add = 0
                        if in_bounds(x1 - diff_x * itx, y1 + diff_y * itx, len_x, len_y):
                            antinodes.append((y1 + diff_y * itx, x1 - diff_x * itx))
                            add += 1
                        if in_bounds(x2 + diff_x * itx, y2 - diff_y * itx, len_x, len_y):
                            antinodes.append((y2 - diff_y * itx, x2 + diff_x * itx))
                            add += 1
                        if not add:
                            break
                        else:
                            itx += 1

        output = len(set(antinodes))
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
    log.log.info(f"Executing Day8 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

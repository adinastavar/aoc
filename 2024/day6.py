"""Code for day 6 of AOC2024"""

import os
import log
import copy

def get_path(cursor, obstacles, max_x, max_y):
    path = set([])

    # going up
    direction = (-1, 0)
    # if you've filled the board, on all 4 directions, it's time to get out
    it = 0
    while 0 <= cursor[0] <= max_y and 0 <= cursor[1] <= max_x:
        if it > max_y * max_x * 4:
            raise TimeoutError
        path.add(cursor)
        next_cursor = (cursor[0] + direction[0], cursor[1] + direction[1])
        if obstacles.get(next_cursor[0], None):
            if next_cursor[1] in obstacles[next_cursor[0]]:
                # change direction
                match direction:
                    case (-1, 0):
                        direction = (0, 1)
                    case (0, 1):
                        direction = (1, 0)
                    case (1, 0):
                        direction = (0, -1)
                    case (0, -1):
                        direction = (-1, 0)
                    case _:
                        raise ValueError("{direction}")
            else:
                cursor = next_cursor
        else:
            cursor = next_cursor
        it += 1

    return path

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
        obstacles = {}
        cursor = (0, 0)

        max_x = 0
        max_y = 0
        for y, line in enumerate(input_data):
            line = line.strip()
            for x, char in enumerate(line):
                if char == '#':
                    if not obstacles.get(y, None):
                        obstacles[y] = [x]
                    else:
                        obstacles[y].append(x)
                elif char == '^':
                    cursor = (int(y), int(x))
                    max_x = len(line)
            max_y = y

        debug = [['.'] * max_x for _ in range(max_y + 1)]
        for y in obstacles:
            for x in obstacles[y]:
                debug[y][x] = '#'

        path = get_path(cursor, obstacles, max_x, max_y)
        output = len(path)

        for p in path:
            debug[p[0]][p[1]] = 'x'

        output_file = os.path.join(os.path.dirname(filename), "debug_" + os.path.basename(filename) + ".txt")
        with open(output_file, "wt", encoding="utf-8") as data:
            for line in debug:
                data.write(" ".join(line) + "\n")

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
        obstacles = {}
        cursor = (0, 0)

        max_x = 0
        max_y = 0
        for y, line in enumerate(input_data):
            for x, char in enumerate(line):
                if char == '#':
                    if not obstacles.get(y, None):
                        obstacles[y] = [x]
                    else:
                        obstacles[y].append(x)
                elif char == '^':
                    cursor = (int(y), int(x))
                    max_x = len(line)
            max_y = y

        path = get_path(cursor, obstacles, max_x, max_y)
        for obstruction in path:
            if obstruction == cursor:
                continue
            new_obstacles = copy.deepcopy(obstacles)
            if not new_obstacles.get(obstruction[0], None):
                new_obstacles[obstruction[0]] = [obstruction[1]]
            else:
                new_obstacles[obstruction[0]].append(obstruction[1])
            try:
                _ = get_path(cursor, new_obstacles, max_x, max_y)
            except TimeoutError:
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
    log.log.info(f"Executing Day6 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

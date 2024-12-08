"""Utility functions for AOC"""
from typing import Tuple

def in_bounds(x : int, y : int, max_x : int, max_y : int) -> bool:
    """Checks if a point is within the map's bounds

    Parameters
    ----------
    x, y : int, int
        Point coordinates
    max_x : int
        Line length (check for x < max_x)
    max_y : int
        Column length (check for y < max_y)

    Returns
    -------
    bool
    """
    if 0 <= x < max_x and 0 <= y < max_y:
        return True
    else:
        return False


def read_as_key_coords(filename) -> Tuple[dict, int, int]:
    """Reads the file input as a dictionary in the form of:
    ```json
    {
        "key1" : [(y1, x1), ..., (yN, xN)],
        ...
        "keyT" : [(y1, x1), ...]
    }
    ```

    Parameters
    ----------
    filename : str
        File to be read

    Returns
    -------
    Tuple[dict, int, int]
        The dictionary, maximum line length, maximum column length
    """
    max_x :int = 0
    max_y :int = 0
    map_dict = {}

    with open(filename, "rt", encoding='utf-8') as input_data:
        for y, line in enumerate(input_data):
            line = line.strip()
            if y == 0:
                max_x = len(line)
            for x, c in enumerate(line):
                if c != '.':
                    if not map_dict.get(c, None):
                        map_dict[c] = [(y, x)]
                    else:
                        map_dict[c].append((y, x))
            max_y += 1

    return map_dict, max_x, max_y

import log
from functools import reduce
from operator import mul

def get_balls(line : str):
    # extract the `Game:` prefix
    game = line.split(":")[-1]
    game = game.replace(";", ",")
    game = game.split(",")
    game = [g.strip() for g in game]
    return game

def main_first_part(filename : str):
    log.log.info("Executing part 1")

    with open(filename, "rt") as input_data:
        MAX : dict = {
            'red'   : 12,
            'green' : 13,
            'blue'  : 14
        }
        sum = 0

        for idx, line in enumerate(input_data):
            is_valid = True
            for s in get_balls(line):
                number, key = s.strip().split(" ")
                if int(number) > MAX[key]:
                    is_valid = False
                    break
            if is_valid:
                sum += (idx + 1)

        log.log.info(f"Day2 result is: {sum}")


def main_second_part(filename : str):
    log.log.info("Executing part 2")

    with open(filename, "rt") as input_data:
        sum = 0

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
            sum += power

        log.log.info(f"Day2 result is: {sum}")

def main(filename : str, part: int):
    log.log.info(f"Executing Day2 for {filename}")
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)
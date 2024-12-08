"""Code for day 7 of AOC2024"""

import log
import itertools
import copy

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
        operators = ['*', '+']
        for line in input_data:
            test_val, eq_members = line.strip().split(':')
            test_val = int(test_val)
            members = [int(m) for m in eq_members.strip().split()]
            op_combinations = [op for op in itertools.product(operators, repeat=len(members) - 1)]

            found =  False
            for opc in op_combinations:
                linesum = 0

                new_list = []
                for i, op in enumerate(opc):
                    new_list.append(members[i])
                    new_list.append(op)
                new_list.append(members[-1])

                linesum = new_list[0]
                for i, elem in enumerate(new_list):
                    if elem == '+':
                        linesum += new_list[i + 1]
                    elif elem == "*":
                        linesum *= new_list[i + 1]

                if linesum == test_val:
                    found = True
                    print(f"{test_val}: {found} {new_list}")

            if found:
                output += test_val

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
        operators = ['*', '+', "||"]
        for line in input_data:
            test_val, eq_members = line.strip().split(':')
            test_val = int(test_val)
            members = [int(m) for m in eq_members.strip().split()]
            op_combinations = [op for op in itertools.product(operators, repeat=len(members) - 1)]

            found =  False
            for opc in op_combinations:
                linesum = 0

                new_list = []
                for i, op in enumerate(opc):
                    new_list.append(members[i])
                    new_list.append(op)
                new_list.append(members[-1])

                linesum = new_list[0]
                for i, elem in enumerate(new_list):
                    if elem == '+':
                        linesum += new_list[i + 1]
                    elif elem == "*":
                        linesum *= new_list[i + 1]
                    elif elem == "||":
                        linesum = int(str(linesum) + str(new_list[i + 1]))

                if linesum == test_val:
                    found = True
                    print(f"{test_val}: {found} {new_list}")

            if found:
                output += test_val
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
    log.log.info(f"Executing Day7 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

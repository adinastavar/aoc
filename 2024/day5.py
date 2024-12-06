"""Code for day 5 of AOC2024"""

import log

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
        rules = {}
        for line in input_data:
            if "|" in line:
                # This is a rule line
                x, y = line.strip().split('|')
                if x in rules:
                    rules[x].append(y)
                else:
                    rules[x] = [y]
            else:
                # Processing the updates
                skip = False
                line = line.strip()
                if not line:
                    skip = True

                pages = line.split(",")
                for idx, pg in enumerate(pages):
                    if pg in rules:
                        for prev_pg in pages[:idx]:
                            if prev_pg in rules[pg]:
                                skip = True
                                break
                if skip is False:
                    output += int(pages[len(pages) // 2])

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

        rules = {}
        for line in input_data:
            if "|" in line:
                # This is a rule line
                x, y = line.strip().split('|')
                if x in rules:
                    rules[x].append(y)
                else:
                    rules[x] = [y]

            else:
                # Processing the updates
                line = line.strip()
                pages = line.split(",")
                if pages == [""]:
                    continue

                add = False

                wrong = True
                while wrong:
                    wrong = False

                    for idx, pg in enumerate(pages):
                        if pg in rules:
                            for prev_pg in pages[:idx]:
                                if prev_pg in rules[pg]:
                                    pages.remove(prev_pg)
                                    pages.insert(idx+1, prev_pg)
                                    wrong = True
                                    add = True
                                    break

                if add:
                    output += int(pages[len(pages) // 2])

        print(rules)

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
    log.log.info(f"Executing Day5 for %s", filename)
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

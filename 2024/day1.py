import log

def main_first_part(filename : str):
    log.log.info("Executing part 1")
    with open(filename, "rt") as input_data:
        sum = 0
        left_list = []
        right_list = []
        for line in input_data:
            n1, n2 = line.strip().split()
            left_list.append(n1)
            right_list.append(n2)

        left_list.sort()
        right_list.sort()

        distances = list(zip(left_list, right_list))
        for dist in distances:
            sum += abs(int(dist[0]) - int(dist[1]))

        log.log.info(f"Day1 result for {filename} is: {sum}")


def main_second_part(filename : str):
    log.log.info("Executing part 2")
    with open(filename, "rt") as input_data:
        sum = 0

        left_list = []
        right_list = []
        for line in input_data:
            n1, n2 = line.strip().split()
            left_list.append(n1)
            right_list.append(n2)

        right_list.sort()

        for left_elem in left_list:
            count_right = 0
            left_num = int(left_elem)

            for right_elem in right_list:
                right_num = int(right_elem)
                if left_num == right_num:
                    count_right += 1
                elif right_num > left_num:
                    break
            sum += left_num * count_right

        log.log.info(f"Day1 result for {filename} is: {sum}")


def main(filename : str, part: int):
    log.log.info(f"Executing Day1 for {filename}")
    match part:
        case 1:
            main_first_part(filename)
        case 2:
            main_second_part(filename)

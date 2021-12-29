# https://adventofcode.com/2021/day/3


def load_file(filename: str) -> list:
    """Load the submarine diagnostic report from  a file

    :param filename: Location of the input file
    :return: List of binary numbers in the report
    """
    with open(filename) as f:
        report = f.read().splitlines()
    return report


def parse_gamma_rate(report: list) -> str:
    report_len = len(report)
    sums = [sum([int(num[j]) for num in report]) for j in range(len(report[0]))]
    gamma_rate = ''
    for i in range(len(report[0])):
        if sums[i] > report_len / 2:
            gamma_rate += '1'
        else:
            gamma_rate += '0'
    return gamma_rate


def get_life_support_rating(report: list, type: str) -> str:
    assert type == 'o2' or type == 'co2'
    report_copy = [num for num in report]
    output = ''
    num_length= len(report[0])
    for j in range(num_length):
        report_len = len(report_copy)
        if report_len == 1:
            return report_copy[0]
        count = sum([int(num[j]) for num in report_copy])
        if count >= report_len / 2:
            delete_flag = str(int(type == 'co2'))
        else:
            delete_flag = str(int(type == 'o2'))
        output += str(int(not bool(int(delete_flag))))
        for i in range(report_len, 0, -1):
            if report_copy[i-1][j] == delete_flag:
                del report_copy[i-1]
    return output
    
    
def solve_part_one(report: list) -> int:
    gamma_rate = parse_gamma_rate(report)
    epsilon_rate = ''.join([str(int(not int(val))) for val in gamma_rate])
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    return gamma_rate * epsilon_rate


def solve_part_two(report: list) -> int:
    o2_generator = get_life_support_rating(report, 'o2')
    co2_scrubber = get_life_support_rating(report, 'co2')
    print(o2_generator)
    print(co2_scrubber)
    return int(o2_generator, 2) * int(co2_scrubber, 2)


def main(depths: list):
    solution_1 = solve_part_one(depths)
    print('Solution to day 03, part 1: {}'.format(solution_1))

    solution_2 = solve_part_two(depths)
    print('Solution to day 03, part 2: {}'.format(solution_2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        parsed_file = load_file(sys.argv[1])
    else:
        parsed_file = load_file('problem03.in')
    main(parsed_file)

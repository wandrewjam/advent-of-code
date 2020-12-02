# https://adventofcode.com/2020/day/1


def load_file(filename: str) -> list:
    """Load the expense report entries from  a file

    :param filename: Location of the input file
    :return: List of expense report entries
    """
    with open(filename) as f:
        entries = f.readlines()
    entries = [int(e) for e in entries]
    return entries


def solve_part_one(report):
    for i, entry1 in enumerate(report[:-1]):
        for entry2 in report[i+1:]:
            if entry1 + entry2 == 2020:
                return entry1 * entry2


def solve_part_two(report):
    for i, entry1 in enumerate(report[:-2]):
        for j, entry2 in enumerate(report[i+1:-1]):
            # Skip the 3rd loop when unnecessary
            if entry1 + entry2 >= 2020:
                continue

            for entry3 in report[i+j+2:]:
                if sum([entry1, entry2, entry3]) == 2020:
                    return entry1 * entry2 * entry3


def main(report: list):
    solution_1 = solve_part_one(report)
    print('Solution to day 01, part 1: {}'.format(solution_1))

    solution_2 = solve_part_two(report)
    print('Solution to day 01, part 2: {}'.format(solution_2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        report = load_file(sys.argv[1])
    else:
        report = load_file('problem01.in')

    main(report)

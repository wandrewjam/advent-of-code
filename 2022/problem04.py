# https://adventofcode.com/2022/day/4


def load_file(filename: str) -> list:
    """Read assignments in file

    :param filename: Location of the input file
    :return: List of assignments
    """
    assignments = []
    with open(filename, encoding="utf_8") as file:
        for line in file:
            left, right = line.rstrip('\n').split(',')
            assignments.append([tuple(int(num) for num in assn.split('-'))
                                for assn in [left,right]])
    return assignments


def solve_part_one(assignments: list) -> int:
    # Count all pairs where one assignment is a subset of the other
    subset_count = 0
    for left_assn, right_assn in assignments:
        if ((left_assn[0] >= right_assn[0]
                and left_assn[1] <= right_assn[1])  # left subset of right
            or (left_assn[0] <= right_assn[0]
                and left_assn[1] >= right_assn[1])):  # vice-versa
            subset_count += 1
    return subset_count


def solve_part_two(assignments: list) -> int:
    # Count all pairs where the assignments overlap at all
    overlap_count = 0
    for left_assn, right_assn in assignments:
        if left_assn[0] <= right_assn[0] <= left_assn[1]:
            overlap_count += 1
        elif left_assn[0] <= right_assn[1] <= left_assn[1]:
            overlap_count += 1
        elif right_assn[0] <= left_assn[0] <= right_assn[1]:
            overlap_count += 1
    return overlap_count


def main(assignments: list):
    solution_1 = solve_part_one(assignments)
    print(f'Solution to day 04, part 1: {solution_1}')

    solution_2 = solve_part_two(assignments)
    print(f'Solution to day 04, part 2: {solution_2}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        parsed_file = load_file(sys.argv[1])
    else:
        parsed_file = load_file('problem04.in')

    main(parsed_file)

# https://adventofcode.com/2021/day/1


def load_file(filename: str) -> list:
    """Load the depth findings from  a file

    :param filename: Location of the input file
    :return: List of depths
    """
    with open(filename) as f:
        depths = f.readlines()
    depths = [int(e) for e in depths]
    return depths


def solve_part_one(depths: list) -> int:
    increased = [d2 > d1 for d1, d2 in zip(depths[:-1], depths[1:])]
    return sum(increased)


def solve_part_two(depths: list) -> int:
    window_sum = [sum(d) for d in zip(depths[:-2], depths[1:-1], depths[2:])]
    increased = [s2 > s1 for s1, s2 in zip(window_sum[:-1], window_sum[1:])]
    return sum(increased)


def main(depths: list):
    solution_1 = solve_part_one(depths)
    print('Solution to day 01, part 1: {}'.format(solution_1))

    solution_2 = solve_part_two(depths)
    print('Solution to day 01, part 2: {}'.format(solution_2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        parsed_file = load_file(sys.argv[1])
    else:
        parsed_file = load_file('problem01.in')

    main(parsed_file)

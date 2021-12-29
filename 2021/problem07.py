# https://adventofcode.com/2021/day/7


def load_file(filename: str) -> list:
    """Load the list of crab positions from filename

    :param filename: Location of the input file
    :return: List of crab positions
    """
    with open(filename) as f:
        crabs = [int(n) for n in f.readline().split(',')]
    crabs.sort()
    return crabs


def solve_part_one(crabs: list) -> int:
    n = len(crabs)
    if n % 2 == 0:
        med = (crabs[n // 2] + crabs[n // 2 - 1]) / 2
    else:
        med = crabs[n // 2]
    fuel = sum([abs(n - med) for n in crabs])
    return fuel


def solve_part_two(crabs: list) -> int:
    mean_fl = int(sum(crabs) / len(crabs))
    fuel_fl = sum([abs(n - mean_fl) * (abs(n - mean_fl) + 1) / 2 for n in crabs])
    fuel_cl = sum([abs(n - mean_fl + 1) * (abs(n - mean_fl + 1) + 1) / 2 for n in crabs])
    return min(fuel_fl, fuel_cl)
    

def main(crabs: list):
    solution_1 = solve_part_one(crabs)
    print('Solution to day 07, part 1: {}'.format(solution_1))

    solution_2 = solve_part_two(crabs)
    print('Solution to day 07, part 2: {}'.format(solution_2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        inputs = load_file(sys.argv[1])
    else:
        inputs = load_file('problem07.in')
    main(inputs)

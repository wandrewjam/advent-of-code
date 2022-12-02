# https://adventofcode.com/2022/day/1


def load_file(filename: str) -> list:
    """Read and sum calories carried by each elf

    :param filename: Location of the input file
    :return: List of calories carried by each elf
    """
    calories_sum = []
    with open(filename) as f:
        calories_per_elf = 0
        for line in f:
            try:
                calories_per_elf += int(line.rstrip('\n'))
            except ValueError:
                calories_sum.append(calories_per_elf)
                calories_per_elf = 0
        calories_sum.append(calories_per_elf)
    return calories_sum


def solve_part_one(calories: list) -> int:
    return max(calories)


def solve_part_two(calories: list) -> int:
    calories.sort(reverse=True)
    return sum(calories[:3])

def main(calories: list):
    solution_1 = solve_part_one(calories)
    print(f'Solution to day 01, part 1: {solution_1}')

    solution_2 = solve_part_two(calories)
    print(f'Solution to day 01, part 2: {solution_2}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        parsed_file = load_file(sys.argv[1])
    else:
        parsed_file = load_file('problem01.in')

    main(parsed_file)

# https://adventofcode.com/2022/day/3


def load_file(filename: str) -> list:
    """Read rucksack contents in file

    :param filename: Location of the input file
    :return: List of contents in each rucksack compartment
    """
    contents = []
    with open(filename, encoding="utf_8") as file:
        for line in file:
            compartment_count = int(len(line.rstrip('\n')) / 2)
            contents.append([line[:compartment_count], line[compartment_count:-1]])
    return contents


def sum_priorities(char_list: list) -> int:
    # Count up the priorities
    priority_sum = 0
    for char in char_list:
        if char.islower():
            priority_sum += ord(char) - 96
        else:
            priority_sum += ord(char) - 64 + 26
    return priority_sum


def solve_part_one(contents: list) -> int:
    # Find common item, stupid way
    common_chars = []
    for left, right in contents:
        for char in left:
            i = right.find(char)
            if i >= 0:
                common_chars.append(char)
                break
    priority_sum = sum_priorities(common_chars)
    return priority_sum


def solve_part_two(contents: list) -> int:
    # Find common item among sets of three
    badges = []
    contents = [left + right for left, right in contents]
    for i in range(0, len(contents), 3):
        for char in contents[i]:
            j = contents[i+1].find(char)
            if j >= 0:
                k = contents[i+2].find(char)
                if k >= 0:
                    badges.append(char)
                    break
    priority_sum = sum_priorities(badges)
    return priority_sum


def main(contents: list):
    solution_1 = solve_part_one(contents)
    print(f'Solution to day 03, part 1: {solution_1}')

    solution_2 = solve_part_two(contents)
    print(f'Solution to day 03, part 2: {solution_2}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        parsed_file = load_file(sys.argv[1])
    else:
        parsed_file = load_file('problem03.in')

    main(parsed_file)

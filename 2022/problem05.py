# https://adventofcode.com/2022/day/5


def load_file(filename: str) -> list:
    """Read crate instructions in file

    :param filename: Location of the input file
    :return: Arrangement of crates and instructions
    """
    crate_arrangement = []
    instructions = []
    is_instruction = False
    with open(filename, encoding="utf_8") as file:
        for line in file:
            if is_instruction:
                split_line = line.split()
                instructions.append((split_line[1], split_line[3], split_line[5]))
            else:
                if len(line) == 1:
                    is_instruction = True
                    continue
                if len(crate_arrangement) == 0:
                    assert len(line) % 4 == 0
                    bins = len(line) // 4
                    crate_arrangement += [[] for _ in range(bins)]
                for i in range(bins):
                    if not line[4*i:4*i+3].isspace() and line[4*i] == '[':
                        crate_arrangement[i].insert(0, line[4*i+1])
    instructions = [(int(a), int(b), int(c)) for a, b, c in instructions]
    return crate_arrangement, instructions


def solve_part_one(crate_arrangement: list, instructions: list) -> str:
    # Rearrange crates according to instructions
    for i, j, k in instructions:
        crate_arrangement[k-1] += [crate_arrangement[j-1].pop() for _ in range(i)]
    crate_str = ''.join([stack[-1] for stack in crate_arrangement])
    return crate_str


def solve_part_two(crate_arrangement: list, instructions: list) -> str:
    # Rearrange crates according to the new procedure
    for i, j, k in instructions:
        crate_arrangement[k-1] += crate_arrangement[j-1][-i:]
        crate_arrangement[j-1][-i:] = []
    crate_str = ''.join([stack[-1] for stack in crate_arrangement])
    return crate_str


def main(crate_arrangement: list, instructions: list):
    crate_copy = [crate[:] for crate in crate_arrangement]
    solution_1 = solve_part_one(crate_arrangement, instructions)
    print(f'Solution to day 05, part 1: {solution_1}')

    solution_2 = solve_part_two(crate_copy, instructions)
    print(f'Solution to day 05, part 2: {solution_2}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        parsed_file = load_file(sys.argv[1])
    else:
        parsed_file = load_file('problem05.in')

    main(*parsed_file)

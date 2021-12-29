# https://adventofcode.com/2021/day/2


def load_file(filename: str) -> list:
    """Load the submarine commands from  a file

    :param filename: Location of the input file
    :return: List of commands
    """
    with open(filename) as f:
        commands = f.readlines()
    commands = [c.split() for c in commands]
    return commands


def solve_part_one(commands: list) -> int:
    end_horz = sum([int(val) for com, val in commands if com == 'forward'])
    end_depth = (sum([int(val) for com, val in commands if com == 'down'])
                 - sum([int(val) for com, val in commands if com == 'up']))
    return end_horz * end_depth


def solve_part_two(commands: list) -> int:
    horz, depth, aim = 0, 0, 0
    for com, val in commands:
        if com == 'down':
            aim += int(val)
        elif com == 'up':
            aim -= int(val)
        elif com == 'forward':
            horz += int(val)
            depth += aim * int(val)
        else:
            raise ValueError('Unexpected command recieved')
    return horz * depth


def main(depths: list):
    solution_1 = solve_part_one(depths)
    print('Solution to day 02, part 1: {}'.format(solution_1))

    solution_2 = solve_part_two(depths)
    print('Solution to day 02, part 2: {}'.format(solution_2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        parsed_file = load_file(sys.argv[1])
    else:
        parsed_file = load_file('problem02.in')

    main(parsed_file)

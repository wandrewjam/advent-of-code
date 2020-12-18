# https://adventofcode.com/2020/day/8


def load_program(filename: str):
    """Load the program from a file

    :param filename: Location of the list of program commands
    :return: Parsed program
    """
    instructions = []
    with open(filename, 'r') as f:
        for line in f:
            operation, argument = line.split()
            instructions.append((operation, int(argument)))
    return instructions


def find_infinite_loop(instructions: list) -> tuple:
    """Find the infinite loop in the program, and return the accumulator

    :param instructions: List of instructions in the program
    :return: Value of the accumulator, and a flag
    """
    accumulator = 0
    line = 0
    line_history = []
    flag = -1
    while line not in line_history:
        try:
            operation, argument = instructions[line]
        except IndexError:
            flag = 0
            return accumulator, flag

        if operation == 'acc':
            accumulator += argument
            line_history.append(line)
            line += 1
        elif operation == 'jmp':
            line_history.append(line)
            line += argument
        elif operation == 'nop':
            line_history.append(line)
            line += 1
    return accumulator, flag


def correct_program(instructions: list) -> int:
    """Figure out how to remove the infinite loop

    :param instructions: List of instructions in the program
    :return: Value of the accumulator
    """
    for i, line in enumerate(instructions):
        operation, argument = line
        instructions_copy = [el for el in instructions]
        if operation == 'jmp':
            instructions_copy[i] = ('nop', argument)
        elif operation == 'nop':
            instructions_copy[i] = ('jmp', argument)
        else:
            continue

        accumulator, flag = find_infinite_loop(instructions_copy)
        if flag == 0:
            return accumulator
    raise ValueError('Reached the end of the program without fixing')


def main(instructions):
    accumulator = find_infinite_loop(instructions)[0]
    print('Solution to 2020 day 08, part 1: {}'.format(accumulator))

    accumulator = correct_program(instructions)
    print('Solution to 2020 day 08, part 2: {}'.format(accumulator))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        program = load_program(sys.argv[1])
    else:
        program = load_program('problem08.in')

    main(program)

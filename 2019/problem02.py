# https://adventofcode.com/2019/day/2


def load_file(filename: str) -> list:
    """Load the Intcode program from a file

    :param filename: Location of the input file
    :return: Parsed Intcode program
    """
    with open(filename) as f:
        raw_program = f.readline()[:-1].split(',')

    program = [int(el) for el in raw_program]
    return program


def write_input(program: list, noun: int = 12, verb: int = 2) -> list:
    """Write to the second and third positions of a program

    :param program: Intcode program to write to
    :param noun: int to write to the first position
    :param verb: int to write to the second position
    :return: Modified Intcode program
    """
    program[1] = noun
    program[2] = verb
    return program


def run_program(program: list) -> int:
    """Execute an Intcode program

    :param program: Intcode program
    :return: Output of the Intcode program
    """
    for i in range(len(program) // 4 + 1):
        opcode = program[4 * i]
        if opcode == 99:
            break
        pos1, pos2, pos3 = program[(4 * i + 1):(4 * i + 4)]
        if opcode == 1:
            program[pos3] = program[pos1] + program[pos2]
        elif opcode == 2:
            program[pos3] = program[pos1] * program[pos2]
        else:
            raise ValueError('Invalid opcode!')
    return program[0]


def run_part_one(program):
    """Run Intcode program with default noun and verb

    :param program: Intcode program
    :return: Output of the Intcode program
    """
    program_copy = [i for i in program]
    write_input(program_copy)
    out = run_program(program_copy)
    return out


def search_input_space(program: list) -> tuple:
    """Search for the noun and verb that produce the target output

    :param program: Intcode program
    :return: Correct noun and verb
    """
    for noun in range(100):
        for verb in range(100):
            program_copy = [i for i in program]
            write_input(program_copy, noun, verb)
            out = run_program(program_copy)
            if out == 19690720:
                return noun, verb


def main(program: list):
    out = run_part_one(program)
    print('Solution to day 02, part 1: {}'.format(out))

    noun, verb = search_input_space(program)
    print('Solution to day 02, part 2: {}'.format(100 * noun + verb))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        int_code = load_file(sys.argv[1])
    else:
        int_code = load_file('problem02.in')

    main(int_code)

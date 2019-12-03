# # https://adventofcode.com/2019/day/2


def load_file(filename: str) -> list:
    with open(filename) as f:
        raw_program = f.readline()[:-1].split(',')

    program = [int(el) for el in raw_program]
    return program


def write_input(program: list, noun: int = 12, verb: int = 2) -> list:
    program[1] = noun
    program[2] = verb
    return program


def run_program(program: list) -> int:
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


def search_input_space(saved_program: list) -> tuple:
    for noun in range(100):
        for verb in range(100):
            program_copy = [i for i in saved_program]
            write_input(program_copy, noun, verb)
            out = run_program(program_copy)
            if out == 19690720:
                return noun, verb


def main(program: list):
    saved_program = [i for i in program]
    write_input(program)
    out = run_program(program)
    print(out)

    noun, verb = search_input_space(saved_program)

    print(100 * noun + verb)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        int_code = load_file(sys.argv[1])
    else:
        int_code = load_file('problem02.in')

    main(int_code)

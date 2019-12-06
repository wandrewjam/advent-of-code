# # https://adventofcode.com/2019/day/5


def load_file(filename: str) -> list:
    with open(filename) as f:
        raw_program = f.readline()[:-1].split(',')

    program = [int(el) for el in raw_program]
    return program


def write_input(program: list, noun: int = 12, verb: int = 2) -> list:
    program[1] = noun
    program[2] = verb
    return program


def get_instructions(code: int) -> list:
    instructions = [int(char) for char in str(code)]
    instructions = [0] * (5 - len(instructions)) + instructions
    return instructions[:3] + [10 * instructions[3] + instructions[4]]


def switch_mode(i1, i2, mode):
    return i1 * (1 - mode) + i2 * mode


def run_program(program: list, input: int):
    i = 0
    while i < len(program):
        mode3, mode2, mode1, op_code = get_instructions(program[i])
        if op_code == 99:
            break
        pos1, pos2, pos3 = [
            switch_mode(program[k], k, mode)
            for k, mode in zip(range(i+1, i+4), [mode1, mode2, mode3])
        ]
        if op_code == 1:
            program[pos3] = program[pos1] + program[pos2]
            i += 4
        elif op_code == 2:
            program[pos3] = program[pos1] * program[pos2]
            i += 4
        elif op_code == 3:
            program[pos1] = input
            i += 2
        elif op_code == 4:
            print(program[pos1])
            i += 2
        elif op_code == 5:
            if program[pos1] == 0:
                i += 3
            else:
                i = program[pos2]

        elif op_code == 6:
            if program[pos1] == 0:
                i = program[pos2]
            else:
                i += 3
        elif op_code == 7:
            if program[pos1] < program[pos2]:
                program[pos3] = 1
            else:
                program[pos3] = 0
            i += 4
        elif op_code == 8:
            if program[pos1] == program[pos2]:
                program[pos3] = 1
            else:
                program[pos3] = 0
            i += 4
        else:
            raise ValueError('Invalid op_code!')


def main(program: list):
    program_copy = [i for i in program]
    run_program(program_copy, input=1)

    print()
    program_copy = [i for i in program]
    run_program(program_copy, input=5)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        int_code = load_file(sys.argv[1])
    else:
        int_code = load_file('problem05.in')

    main(int_code)

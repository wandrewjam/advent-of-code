# # https://adventofcode.com/2019/day/2


def load_file(filename: str) -> list:
    with open(filename) as f:
        raw_program = f.readline()[:-1].split(',')

    program = [int(el) for el in raw_program]
    return program


def main(program: list):
    for i in range(len(program) // 4 + 1):
        opcode = program[4 * i]
        if opcode == 99:
            print('Break!')
            break
        pos1, pos2, pos3 = program[(4 * i + 1):(4 * i + 4)]
        if opcode == 1:
            program[pos3] = program[pos1] + program[pos2]
        elif opcode == 2:
            program[pos3] = program[pos1] * program[pos2]
        else:
            raise ValueError('Invalid opcode!')

    print(program)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        int_code = load_file(sys.argv[1])
    else:
        int_code = load_file('problem02.in')
        int_code[1] = 12
        int_code[2] = 2

    main(int_code)

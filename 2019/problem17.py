# https://adventofcode.com/2019/day/17
import matplotlib.pyplot as plt
import numpy as np


def load_file(filename: str) -> list:
    with open(filename) as f:
        program = f.readline()[:-1].split(',')
    program = [int(char) for char in program]
    return program


def get_instructions(code: int) -> list:
    instructions = [int(char) for char in str(code)]
    instructions = [0] * (5 - len(instructions)) + instructions
    return instructions[:3] + [10 * instructions[3] + instructions[4]]


def switch_mode(i0, i1, i2, mode):
    return i0 * (mode == 0) + i1 * (mode == 1) + i2 * (mode == 2)


def run_program(program: list, inputs: list, i: int = 0,
                rel_base: int = 0) -> tuple:
    input_count = 0
    output = list()
    while True:
        mode3, mode2, mode1, op_code = get_instructions(program[i])

        if op_code == 99:
            status = 1
            return output, status, i, rel_base

        pos1, pos2, pos3 = [
            switch_mode(program[k], k, rel_base + program[k], mode)
            if k < len(program) else -1
            for k, mode in zip(range(i+1, i+4), [mode1, mode2, mode3])
        ]

        if op_code == 1:
            program[pos3] = program[pos1] + program[pos2]
            i += 4
        elif op_code == 2:
            program[pos3] = program[pos1] * program[pos2]
            i += 4
        elif op_code == 3:
            if input_count < len(inputs):
                program[pos1] = inputs[input_count]
                input_count += 1
                i += 2
            elif input_count == len(inputs):
                status = 0
                return output, status, i, rel_base
            else:
                raise ValueError('Error in the inputs')
        elif op_code == 4:
            i += 2
            output.append(program[pos1])
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
        elif op_code == 9:
            rel_base += program[pos1]
            i += 2
        else:
            raise ValueError('Invalid op_code!')


def process_output(output):
    out_array = list()
    line = list()
    pointer_codes = [ord('<'), ord('>'), ord('^'), ord('v')]
    for code in output:
        if code == 10:
            out_array.append([char for char in line])
            line = list()
        elif code == 35 or code in pointer_codes:
            line.append(1)
        elif code == 46:
            line.append(0)
        else:
            raise ValueError('Invalid code!')
    return out_array


def find_intersections(out_array) -> list:
    # Pad the out array with zeros
    num_rows, num_cols = len(out_array), len(out_array[0])
    out_array.insert(0, [0 for _ in range(num_cols)])
    out_array.append([0 for _ in range(num_cols)])
    for line in out_array:
        line.append(0)
        line.insert(0, 0)
        assert len(line) == num_cols + 2

    intersections = list()
    for i, line in enumerate(out_array[1:-1]):
        for j, col in enumerate(line[1:-1]):
            if (line[j] == 1 and line[j + 1] == 1 and line[j+2] == 1
                    and out_array[i][j+1] == 1 and out_array[i+2][j+1] == 1):
                intersections.append((i, j))
    return intersections


def main(program: list):
    program_copy = [k for k in program]
    program_copy += [0 for _ in range((2 ** 3 - 1) * len(program))]
    output, status, i, rel_base = run_program(program_copy, [])
    out_array = process_output(output[:-1])
    intersections = find_intersections(out_array)
    alignment_parameters = [point[0] * point[1] for point in intersections]
    print(sum(alignment_parameters))

    # Test
    # out_array = list()
    # with open('problem17_test1.in') as f:
    #     for line in f:
    #         codes = [ord(char) for char in line[:-1]]
    #         out_array.append([int(code == 35) for code in codes])
    #
    # intersections = find_intersections(out_array)
    # print(intersections)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        raw_program = load_file(sys.argv[1])
    else:
        raw_program = load_file('problem17.in')

    main(raw_program)

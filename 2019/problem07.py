# https://adventofcode.com/2019/day/6
from itertools import permutations


def load_file(filename: str) -> list:
    with open(filename) as f:
        program = f.readline()[:-1].split(',')
    program = [int(char) for char in program]
    return program


def get_instructions(code: int) -> list:
    instructions = [int(char) for char in str(code)]
    instructions = [0] * (5 - len(instructions)) + instructions
    return instructions[:3] + [10 * instructions[3] + instructions[4]]


def switch_mode(i1, i2, mode):
    return i1 * (1 - mode) + i2 * mode


def run_program(program: list, inputs: list, i: int = 0) -> tuple:
    input_count = 0
    while i < len(program):
        mode3, mode2, mode1, op_code = get_instructions(program[i])
        if op_code == 99:
            return None, 1, -1

        pos1, pos2, pos3 = [
            switch_mode(program[k], k, mode)
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
            program[pos1] = inputs[input_count]
            input_count += 1
            i += 2
        elif op_code == 4:
            i += 2
            status = 0
            return program[pos1], status, i
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


def run_amplifier_sequence(program: list, phase_setting: tuple) -> int:
    input_instruction = 0
    for setting in phase_setting:
        program_copy = [i for i in program]
        input_instruction = run_program(
            program_copy, [setting, input_instruction]
        )[0]
    return input_instruction


def run_feedback_loop(program: list, phase_setting: tuple) -> int:
    status = 0
    input_instruction = 0
    execution_point = [0 for _ in range(len(phase_setting))]
    final_output = None
    program_copies = [[i for i in program] for _ in range(len(phase_setting))]
    for j, setting in enumerate(phase_setting):
        input_instruction, status, execution_point[j] = run_program(
            program_copies[j], [setting, input_instruction], execution_point[j]
        )

    while status != 1:
        for j in range(len(phase_setting)):
            input_instruction, status, execution_point[j] = run_program(
                program_copies[j], [input_instruction], execution_point[j]
            )
        if status == 0:
            final_output = input_instruction
    return final_output


def main(program: list):
    phase_settings = list(permutations(range(5)))
    max_output = 0
    max_setting = None
    for setting in phase_settings:
        output = run_amplifier_sequence(program, setting)
        if max_output < output:
            max_output = output
            max_setting = setting
    print(max_output, max_setting)

    phase_settings = list(permutations(range(5, 10)))
    max_output = 0
    max_setting = None
    for setting in phase_settings:
        output = run_feedback_loop(program, setting)
        if output > max_output:
            max_output = output
            max_setting = setting

    print(max_output, max_setting)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        raw_program = load_file(sys.argv[1])
    else:
        raw_program = load_file('problem07.in')

    main(raw_program)

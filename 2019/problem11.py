# https://adventofcode.com/2019/day/11
import matplotlib.pyplot as plt


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


def run_painting_robot(program, start_color=0) -> dict:
    program_copy = [i for i in program]
    program_copy += [0 for _ in range((2 ** 3 - 1) * len(program_copy))]
    past_locations = {(0, 0): start_color}
    robot_location = (0, 0)
    robot_facing = (0, 1)
    i, rel_base = 0, 0
    while True:
        try:
            input = past_locations[robot_location]
        except KeyError:
            input = 0
            past_locations[robot_location] = 0
        output, status, i, rel_base = run_program(program_copy, [input],
                                                  i, rel_base)
        if status == 1:
            break

        past_locations[robot_location] = output[0]
        if output[1] == 0:
            robot_facing = (-robot_facing[1], robot_facing[0])
        elif output[1] == 1:
            robot_facing = (robot_facing[1], -robot_facing[0])
        else:
            raise ValueError('output is invalid')

        robot_location = (robot_location[0] + robot_facing[0],
                          robot_location[1] + robot_facing[1])
    return past_locations


def show_result(locations: dict):
    x_coords, y_coords = list(zip(*locations.keys()))
    minx, maxx = min(x_coords), max(x_coords)
    miny, maxy = min(y_coords), max(y_coords)
    hull = [[0 for _ in range(minx, maxx+1)] for _ in range(miny, maxy+1)]
    for location, color in locations.items():
        hull[location[1] - miny][location[0] - minx] = color

    plt.imshow(hull, cmap='binary', origin='lower')
    plt.show()


def main(program: list):
    gibberish = run_painting_robot(program, start_color=0)
    registration = run_painting_robot(program, start_color=1)
    show_result(gibberish)
    show_result(registration)



if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        raw_program = load_file(sys.argv[1])
    else:
        raw_program = load_file('problem11.in')

    main(raw_program)

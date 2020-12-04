# https://adventofcode.com/2019/day/15
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


def search(area, visited: set, position: np.ndarray, program_copy, i, rel_base):
    visited.add(tuple(position))
    north = position + [-1, 0]
    south = position + [1, 0]
    east = position + [0, 1]
    west = position + [0, -1]
    adjacent = {1: north, 2: south, 3: west, 4: east}
    for direction, check_location in adjacent.items():
        if area[check_location[0], check_location[1]] == -1:
            inputs = [direction]
            output, status, i, rel_base = run_program(program_copy, inputs, i, rel_base)
            area[adjacent[direction][0], adjacent[direction][1]] = output[-1]
            pos_array = np.zeros(shape=area.shape)
            pos_array[position[0], position[1]] = 2
            if output[-1] == 0:
                continue
            position = adjacent[direction]
            search(area, visited, position, program_copy, i, rel_base)
            # Navigate back
            if direction == 1:
                inputs = [2]
            elif direction == 2:
                inputs = [1]
            elif direction == 3:
                inputs = [4]
            elif direction == 4:
                inputs = [3]
            output, status, i, rel_base = run_program(program_copy, inputs, i, rel_base)


def find_path_length(area: np.ndarray) -> int:
    source = np.where(area == 3)
    oxygen = np.where(area == 2)
    adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = np.zeros(shape=area.shape, dtype=bool)
    visited[source] = True
    q_list = [(source, 0)]

    while len(q_list) > 0:
        current_point, current_distance = q_list[0]
        if current_point == oxygen:
            return current_distance
        del q_list[0]

        for i in range(4):
            next_point = tuple(current_coord + next_coord for current_coord, next_coord in zip(current_point, adjacent[i]))
            if area[next_point] > 0 and not visited[next_point]:
                visited[next_point] = True
                q_list.append((next_point, current_distance + 1))


def fill_with_oxygen(area: np.ndarray, time_elapsed: int) -> int:
    adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    row, col = np.where(area == 2)
    while 1 in area:
        for i in range(len(row)):
            for j in adjacent:
                if area[row[i] + j[0], col[i] + j[1]] == 1:
                    area[row[i] + j[0], col[i] + j[1]] += 1
        time_elapsed += 1
        row, col = np.where(area == 2)
    return time_elapsed


def main(program: list):
    program_copy = [i for i in program]
    program_copy += [0 for _ in range(len(program) * (2**3 - 1))]

    # Explore area
    area = -np.ones(shape=(2**6 - 1,) * 2)
    position = np.array([2**5 - 1, 2**5 - 1])
    area[position[0], position[1]] = 1
    i, rel_base = 0, 0
    search(area, set(), position, program_copy, i, rel_base)
    area[position[0], position[1]] += 2
    plt.imshow(area)
    plt.show()
    shortest_path = find_path_length(area)
    print(np.where(area == 2))
    print(np.where(area == 3))
    print(shortest_path)

    time_to_fill = fill_with_oxygen(area, 0)
    print(time_to_fill)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        raw_program = load_file(sys.argv[1])
    else:
        raw_program = load_file('problem15.in')

    main(raw_program)

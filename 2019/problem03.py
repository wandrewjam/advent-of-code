# https://adventofcode.com/2019/day/3


def load_file(filename: str) -> list:
    with open(filename) as f:
        raw_instructions = f.readlines()
    instructions = [path.split(',') for path in raw_instructions]
    return instructions


def parse_path(instructions: list) -> list:
    path = [(0, 0)]
    for instruction in instructions:
        direction = instruction[0]
        value = int(instruction[1:])
        old_x, old_y = path[-1]
        if direction == 'R':
            new_x = old_x + value
            new_y = old_y
        elif direction == 'L':
            new_x = old_x - value
            new_y = old_y
        elif direction == 'U':
            new_x = old_x
            new_y = old_y + value
        elif direction == 'D':
            new_x = old_x
            new_y = old_y - value
        else:
            raise ValueError('Invalid direction!')
        path.append((new_x, new_y))
    return path


def test_for_intersection(segment1: list, segment2: list) -> tuple:
    tmp = [*segment1, *segment2]
    x, y = zip(*tmp)
    if x[0] == x[1]:  # First segment vertical
        if min(x[2:]) < x[0] < max(x[2:]):
            if min(y[:2]) < y[2] < max(y[:2]):
                # Calculate intersection
                int_x, int_y = x[0], y[2]
                return int_x, int_y
            else:
                return tuple()
        else:
            return tuple()
    elif y[0] == y[1]:  # First segment horizontal
        if min(y[2:]) < y[0] < max(y[2:]):
            if min(x[:2]) < x[2] < max(x[:2]):
                # Calculate intersection
                int_x, int_y = x[2], y[0]
                return int_x, int_y
            else:
                return tuple()
        else:
            return tuple()


def find_intersections(paths_list: list) -> list:
    intersections = list()
    for i in range(len(paths_list[0]) - 1):
        for j in range(len(paths_list[1]) - 1):
            segment1 = paths_list[0][i:i+2]
            segment2 = paths_list[1][j:j+2]
            intersection = test_for_intersection(segment1, segment2)
            if len(intersection) > 0:
                intersections.append(intersection)

    return intersections


def find_path_length(path: list, intersection: tuple) -> int:
    distance_traveled = 0
    int_x, int_y = intersection
    for i in range(len(path) - 1):
        curr_x, curr_y = path[i]
        next_x, next_y = path[i+1]
        if int_x == curr_x:
            if (int_x == next_x
                    and min(curr_y, next_y) < int_y < max(curr_y, next_y)):
                distance_traveled += abs(int_x - curr_x) + abs(int_y - curr_y)
                return distance_traveled
            else:
                distance_traveled += (abs(next_x - curr_x)
                                      + abs(next_y - curr_y))
        elif int_y == curr_y:
            if (int_y == next_y
                    and min(curr_x, next_x) < int_x < max(curr_x, next_x)):
                distance_traveled += abs(int_x - curr_x) + abs(int_y - curr_y)
                return distance_traveled

            else:
                distance_traveled += (abs(next_x - curr_x)
                                      + abs(next_y - curr_y))
        else:
            distance_traveled += abs(next_x - curr_x) + abs(next_y - curr_y)


def main(instructions_list: list):
    paths_list = list()
    for instructions in instructions_list:
        paths_list.append(parse_path(instructions))

    intersections = find_intersections(paths_list)
    distances = [abs(point[0]) + abs(point[1]) for point in intersections]
    print(min(distances))

    length_sums = list()
    for intersection in intersections:
        path_lengths = [find_path_length(path, intersection)
                        for path in paths_list]
        length_sums.append(sum(path_lengths))

    print(min(length_sums))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        paths = load_file(sys.argv[1])
    else:
        paths = load_file('problem03.in')

    main(paths)

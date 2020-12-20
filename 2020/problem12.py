# https://adventofcode.com/2020/day/12


def load_instructions(filename: str) -> list:
    """Load the seating arrangement from a file

    :param filename: Location of the seat arrangement file
    :return: List of seats
    """
    with open(filename, 'r') as f:
        instructions = []
        for line in f:
            instructions.append([line[0], int(line[1:])])
    return instructions


def move_ship_waypoint(instructions: list) -> list:
    """Move the ship using the waypoint movement rules

    :param instructions: List of movement instructions
    :return: Final position of the ship
    """
    waypoint = [10, 1]
    ship = [0, 0]
    for instruction in instructions:
        cmd, val = instruction

        if cmd == 'F':
            ship[0] += val * waypoint[0]
            ship[1] += val * waypoint[1]

        if cmd == 'N':
            waypoint[1] += val
        elif cmd == 'S':
            waypoint[1] -= val
        elif cmd == 'E':
            waypoint[0] += val
        elif cmd == 'W':
            waypoint[0] -= val
        elif cmd == 'L' or cmd == 'R':
            rotation = (2 * (cmd == 'L') - 1) * val % 360
            if rotation == 90:
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
            elif rotation == 180:
                waypoint[0] *= -1
                waypoint[1] *= -1
            elif rotation == 270:
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    return ship


def move_ship(instructions: list) -> list:
    """Move the ship using the facing direction movement rules

    :param instructions: List of movement instructions
    :return: Final position of the ship
    """
    position = [0, 0]
    direction = 0
    for instruction in instructions:
        cmd, val = instruction

        if cmd == 'F' and direction == 0:
            cmd = 'E'
        elif cmd == 'F' and direction == 90:
            cmd = 'N'
        elif cmd == 'F' and direction == 180:
            cmd = 'W'
        elif cmd == 'F' and direction == 270:
            cmd = 'S'

        if cmd == 'N':
            position[1] += val
        elif cmd == 'S':
            position[1] -= val
        elif cmd == 'E':
            position[0] += val
        elif cmd == 'W':
            position[0] -= val
        elif cmd == 'L':
            direction += val
            direction %= 360
        elif cmd == 'R':
            direction -= val
            direction %= 360
    return position


def main(instructions: list):
    position1 = move_ship(instructions)
    distance1 = abs(position1[0]) + abs(position1[1])
    print('Solution to 2020 day 12, part 1: {}'.format(distance1))
    position2 = move_ship_waypoint(instructions)
    distance2 = abs(position2[0]) + abs(position2[1])
    print('Solution to 2020 day 12, part 2: {}'.format(distance2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        instructions_list = load_instructions(sys.argv[1])
    else:
        instructions_list = load_instructions('problem12.in')

    main(instructions_list)

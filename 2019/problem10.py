# https://adventofcode.com/2019/day/10
from math import gcd, atan2


def load_file(filename: str) -> list:
    with open(filename) as f:
        field = f.readlines()
    field = [[1 if point == '#' else 0 for point in line[:-1]]
             for line in field]
    return field


def get_visible(asteroid, asteroid_locations):
    visible = dict()
    for point in asteroid_locations:
        divisor = gcd(point[0] - asteroid[0], point[1] - asteroid[1])
        if divisor > 0:
            sight = ((point[0] - asteroid[0]) / divisor,
                     (point[1] - asteroid[1]) / divisor)
            if sight not in visible.keys():
                visible[sight] = point
            elif (abs(visible[sight][0] - asteroid[0])
                  > abs(point[0] - asteroid[0])):
                visible[sight] = point
    return visible.values()


def vaporize_asteroids(asteroid, asteroid_locations):
    vaporized = list()
    while len(asteroid_locations) > 1:
        currently_visible = get_visible(asteroid, asteroid_locations)
        thetas = [atan2(-point[0] + asteroid[0], point[1] - asteroid[1])
              for point in currently_visible]
        thetas_visible = sorted(list(zip(currently_visible, thetas)),
                                key=lambda p: p[1])
        if thetas_visible[-1][0][0] == asteroid[0]:
            thetas_visible = [thetas_visible[-1]] + thetas_visible[:-1]
        vaporized += list(zip(*thetas_visible))[0]
        asteroid_locations = list(set(asteroid_locations)
                                  - set(currently_visible))
    return vaporized


def main(field: list):
    asteroid_locations = list()
    for j, line in enumerate(field):
        for i, point in enumerate(line):
            if point == 1:
                asteroid_locations.append((i, j))

    max_visible = 0
    max_point = (-1, -1)
    for asteroid in asteroid_locations:
        visible = len(get_visible(asteroid, asteroid_locations))
        if visible > max_visible:
            max_point = asteroid
            max_visible = visible
    print(max_point)
    print(max_visible)

    vaporized = vaporize_asteroids(max_point, asteroid_locations)
    print(vaporized[199])


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        asteroid_field = load_file(sys.argv[1])
    else:
        asteroid_field = load_file('problem10.in')

    main(asteroid_field)

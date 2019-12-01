# https://adventofcode.com/2018/day/6
# import matplotlib.pyplot as plt
# import numpy as np


def load_file(filename: str) -> list:
    points = list()
    with open(filename) as f:
        points_raw = f.readlines()

    for point_raw in points_raw:
        point = list()
        for coordinate in point_raw.split(', '):
            point.append(int(coordinate))
        points.append(tuple(point))
    return points


def distance(pt1: tuple, pt2: tuple) -> int:
    x1, y1 = pt1
    x2, y2 = pt2
    return abs(x1 - x2) + abs(y1 - y2)


def find_closest_point(pt: tuple, pts: list) -> int:
    distances = dict()
    for i in range(len(pts)):
        distances[i] = distance(pt, pts[i])

    min_dist = max(distances.values()) + 1
    min_key = -1
    for (key, value) in distances.items():
        if value < min_dist:
            min_dist = value
            min_key = key
        elif value == min_dist:
            min_key = None
    assert min_key != -1
    return min_key


def find_total_distance(pt: tuple, pts: list) -> int:
    total_distance = 0
    for point in pts:
        total_distance += distance(pt, point)
    return total_distance


def main(pts: list):
    # Exclude the points with infinite domains
    # Assemble the points on the boundary
    x_coordinates, y_coordinates = zip(*pts)
    min_x, max_x = min(x_coordinates), max(x_coordinates)
    min_y, max_y = min(y_coordinates), max(y_coordinates)
    bdy = set()
    for x in [min_x, max_x]:
        for y in range(min_y, max_y + 1):
            bdy.add((x, y))

    for y in [min_y, max_y]:
        for x in range(min_x, max_x + 1):
            bdy.add((x, y))

    excluded_points = set()
    for pt in bdy:
        excluded_points.add(find_closest_point(pt, pts))

    included_points = set(range(len(pts))) - set(excluded_points)
    areas = dict(zip(included_points, (0,)*len(included_points)))

    # closest_points = np.zeros(shape=(max_x - min_x + 1, max_y - min_y + 1))
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            closest_pt = find_closest_point((x, y), pts)
            # closest_points[i, j] = closest_pt
            if closest_pt in areas.keys():
                areas[closest_pt] += 1

    # point_array = np.array(pts)
    # plt.imshow(closest_points.T, extent=[min_x - .5, max_x + .5, max_y + .5, min_y - .5])
    # plt.scatter(point_array[:, 0], point_array[:, 1], c='k')
    # plt.show()
    print(max(areas.values()))

    distance_threshold = 10000
    threshold_area = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            total_distance = find_total_distance((x, y), pts)
            if total_distance < distance_threshold:
                threshold_area += 1
    print(threshold_area)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        points = load_file(sys.argv[1])
    else:
        points = load_file('problem06.in')

    main(points)

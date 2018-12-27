# https://adventofcode.com/2018/day/2


def load_file(file) -> list:
    """
    Reads a file containing a list of rectangle definitions, and returns
        a list with the rectangle specs. The ID is the array location
    :param file: Text file containing a rectangle definition on each
        line
    :return: List with parsed rectangle definition
    """
    import re
    rectangles = list()
    with open(file) as f:
        for line in f:
            rectangles.append(re.split('\D+', line)[2:-1])

    for i in range(len(rectangles)):
        for j in range(4):
            rectangles[i][j] = int(rectangles[i][j])
    return rectangles


def solve_part_one(rectangles: list, side: int) -> int:
    """
    Calculates the total area of overlapping claims
    :param rectangles: List of rectangle claims
    :param side: Maximum side length
    :return: Area of overlapping claims
    """
    cloth = [[0]*side for _ in range(side)]
    for rectangle in rectangles:
        for i in range(rectangle[2]):
            for j in range(rectangle[3]):
                cloth[rectangle[0] + i][rectangle[1] + j] += 1

    area = 0
    for row in cloth:
        for col in row:
            area += (col >= 2)

    return area


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        rectangles = load_file(sys.argv[1])
    else:
        rectangles = load_file('problem03.in')

    SIDE_LENGTH = 1000
    overlap_area = solve_part_one(rectangles, SIDE_LENGTH)

    print(overlap_area)

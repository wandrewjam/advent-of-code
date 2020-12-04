# https://adventofcode.com/2020/day/3


def load_file(filename):
    """Load the area map

    :param filename: Location of the input file
    :return: List of lines of the map
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line[:-1] for line in lines]
    return lines


def count_trees(area_data: list, down: int, right: int) -> int:
    """Count the trees you would hit on a straight trajectory

    :param area_data: List containing a map of tree locations
    :param down: Number of units down per step
    :param right: Number of units right per step
    :return: Total number of trees hit
    """
    width = len(area_data[0])
    count = 0
    for i, line in enumerate(area_data[::down]):
        count += line[(right * i) % width] == '#'
    return count


def main(area_data):
    count = count_trees(area_data, 1, 3)
    print('Solution to 2020 day 03, problem 1: {}'.format(count))
    print('Solution to 2020 day 03, problem 2: {}'.format(
        count_trees(area_data, 1, 1) * count_trees(area_data, 1, 3)
        * count_trees(area_data, 1, 5) * count_trees(area_data, 1, 7)
        * count_trees(area_data, 2, 1)
    ))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        area = load_file(sys.argv[1])
    else:
        area = load_file('problem03.in')

    main(area)

# https://adventofcode.com/2020/day/6


def load_file(filename: str) -> list:
    """Read file containing survey responses

    :param filename: Location of survey response file
    :return: List of survey responses by group
    """
    groups = []
    gp = []
    with open(filename, 'r') as f:
        for line in f:
            if line == '\n':
                groups.append(gp)
                gp = []
            else:
                gp.append(frozenset(line[:-1]))
    groups.append(gp)
    return groups


def main(group_list: list):
    group_sum1 = sum([len(frozenset.union(*group)) for group in group_list])
    print('Solution to 2020 day 06, part 1: {}'.format(group_sum1))

    group_sum2 = sum([len(frozenset.intersection(*group))
                      for group in group_list])
    print('Solution to 2020 day 06, part 2: {}'.format(group_sum2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        groups = load_file(sys.argv[1])
    else:
        groups = load_file('problem06.in')

    main(groups)

# https://adventofcode.com/2018/day/2


def load_file(file: str) -> list:
    """
    Reads a file containing a list of IDs, and returns a python list
    of strings
    :param file: Text file containing an ID on each line
    :return: Python list of ID strings
    """
    with open(file) as f:
        id_list = f.readlines()
    return id_list


def solve_part_one(id_list: list) -> int:
    """
    Calculates the checksum for a list of IDs
    :param id_list: Python list containing a list of ID strings
    :return: Checksum as defined by the problem
    """
    from collections import Counter

    twos, threes = 0, 0
    for id in id_list:
        id_counter = Counter(id)
        if 2 in id_counter.values():
            twos += 1
        if 3 in id_counter.values():
            threes += 1

    checksum = twos * threes

    return checksum


def solve_part_two(id_list: list) -> str:
    """
    Finds the two IDs that differ by exactly one character.
    Assumptions: there is exactly one pair of IDs that differ by one
        character
    :param id_list: Python list of ID strings
    :return: String of common letters between the two correct IDs
    """
    length = len(id_list)
    for i in range(length-1):
        for j in range(i+1, length):
            first_id, second_id = id_list[i], id_list[j]
            common = list()
            for k in range(len(first_id)):
                if first_id[k] == second_id[k]:
                    common.append(first_id[k])
            if len(common) == len(first_id) - 1:
                return ''.join(common)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        id_list = load_file(sys.argv[1])
    else:
        id_list = load_file('problem02.in')

    checksum = solve_part_one(id_list)
    letters = solve_part_two(id_list)

    print('The checksum is: {:d}'.format(checksum))
    print('The common letters are: {:s}'.format(letters))

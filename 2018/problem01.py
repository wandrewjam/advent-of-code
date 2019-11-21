# https://adventofcode.com/2018/day/1


def load_file(file: str) -> list:
    """
    Loads a list of frequency changes and returns a list of integers
    :param file: Name of file containing list of integers
    :return: Python list of integers in the file
    """
    with open(file) as f:
        frequency_string = f.read().split()

    frequency_list = [int(el) for el in frequency_string]

    return frequency_list


def solve_part_one(sequence: list) -> int:
    """
    Calculates the final frequency after all changes are applied
    :param sequence: Python list of integer frequency changes
    :return: Final frequency
    """

    final_frequency = 0
    for change in sequence:
        final_frequency += change

    return final_frequency


def solve_part_two(sequence: list) -> int:
    """
    Calculates the first frequency that occurs twice
    :param sequence: Python list of integer frequency changes
    :return: First repeated frequency
    """

    frequencies = {0}
    counter = 0
    current = 0
    while True:
        current += sequence[counter]
        if current in frequencies:
            break
        else:
            frequencies.add(current)
            counter += 1
            counter %= len(sequence)

    return current


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        sequence = load_file(sys.argv[1])
    else:
        sequence = load_file('problem01.in')

    final_frequency = solve_part_one(sequence)
    first_frequency = solve_part_two(sequence)

    print('Final frequency after applying all changes once: {:d}'
          .format(final_frequency))
    print('First frequency reached twice: {:d}'.format(first_frequency))

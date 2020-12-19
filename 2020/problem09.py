# https://adventofcode.com/2020/day/9


def load_data(filename: str) -> list:
    """Load the data from a file

    :param filename: Path to the data file
    :return: Parsed data
    """
    with open(filename, 'r') as f:
        xmas = f.readlines()
    xmas = [int(x) for x in xmas]
    return xmas


def find_invalid(xmas: list) -> int:
    preamble = 25
    for i, x in enumerate(xmas[preamble:]):
        is_valid = False
        for j1 in range(preamble):
            for j2 in range(j1 + 1, preamble):
                if x == xmas[j1 + i] + xmas[j2 + i]:
                    is_valid = True
                if is_valid:
                    break
            if is_valid:
                break
        if not is_valid:
            return x
    return -1


def find_sequence(xmas: list, value: int) -> int:
    sequence_length = 1
    while True:
        sequence_length += 1
        for i in range(len(xmas) - sequence_length):
            sequence = xmas[i:i + sequence_length]
            if value == sum(sequence):
                return min(sequence) + max(sequence)
        if sequence_length >= len(xmas):
            return -1


def main(xmas: list):
    val = find_invalid(xmas)
    print('Solution to 2020 day 09, part 1: {}'.format(val))
    sequence_sum = find_sequence(xmas, val)
    print('Solution to 2020 day 09, part 2: {}'.format(sequence_sum))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        data = load_data(sys.argv[1])
    else:
        data = load_data('problem09.in')

    main(data)

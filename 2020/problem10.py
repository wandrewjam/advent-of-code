# https://adventofcode.com/2020/day/10


def load_voltages(filename: str) -> list:
    """Load the adapter voltages from an input file

    :param filename: Location of the voltage file
    :return: List of adapter voltages
    """
    with open(filename, 'r') as f:
        voltages = f.readlines()
    voltages = [int(v) for v in voltages]
    return voltages


def find_differences(voltages: list) -> tuple:
    """Count all the differences of 1 and 3 voltages

    :param voltages: List of adapter voltages
    :return: Counts of 1-differences and 3-differences
    """
    voltages.append(0)
    voltages.append(max(voltages) + 3)
    voltages.sort()
    differences = [voltages[i+1] - voltages[i]
                   for i in range(len(voltages) - 1)]
    one_differences = 0
    three_differences = 0
    for diff in differences:
        one_differences += diff == 1
        three_differences += diff == 3
    return one_differences, three_differences


def count_sub_arrangements(sublist: list) -> int:
    """Count all possible arrangements of a given sublist

    :param sublist: Sublist of possible adapters
    :return: Count of all valid arrangements of sublists
    """
    candidate_count = 2 ** (len(sublist) - 2)
    if candidate_count == 1:
        return 1
    else:
        valid_count = 0
        for i in range(candidate_count):
            bin_i = format(i, 'b')
            bin_i = '0' * (len(sublist) - len(bin_i) - 2) + bin_i
            bin_i = '1' + bin_i + '1'
            candidate = [sublist[j] for j in range(len(sublist))
                         if bin_i[j] == '1']
            diffs = [candidate[i+1] - candidate[i]
                     for i in range(len(candidate) - 1)]
            valid_count += (max(diffs) <= 3)

        return valid_count


def count_arrangements(voltages: list) -> int:
    """Count all possible adapter arrangements

    :param voltages: List of adapter voltages
    :return: Count of all possible arrangements
    """
    voltages.sort()
    diffs = [voltages[i+1] - voltages[i] for i in range(len(voltages) - 1)]
    cumulative_diffs = [diffs[i+1] + diffs[i] for i in range(len(diffs) - 1)]
    is_necessary = [diff > 3 for diff in cumulative_diffs]
    is_necessary.append(True)
    is_necessary.insert(0, True)
    necessary_indices = [i for i in range(len(is_necessary))
                         if is_necessary[i]]
    sublists = []
    for i in range(len(necessary_indices) - 1):
        sublists.append(voltages[necessary_indices[i]:
                                 necessary_indices[i+1]+1])
    sub_counts = [count_sub_arrangements(sub) for sub in sublists]
    product = 1
    for count in sub_counts:
        product *= count
    return product


def main(voltages: list):
    ones, threes = find_differences(voltages)
    print('Solution to 2020 day 10, part 1: {}'.format(ones * threes))
    arrangements = count_arrangements(voltages)
    print('Solution to 2020 day 10, part 2: {}'.format(arrangements))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        data = load_voltages(sys.argv[1])
    else:
        data = load_voltages('problem10.in')

    main(data)

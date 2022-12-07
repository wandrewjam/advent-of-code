# https://adventofcode.com/2022/day/6


def load_file(filename: str) -> str:
    """Read signals from file

    :param filename: Location of the input file
    :return: String representing the datastream
    """
    with open(filename, encoding="utf_8") as file:
        signal = file.readline()
    return signal


def solve_part_one(signal: list) -> int:
    # Finds the start-of-packet marker in the signal
    for i in range(len(signal) - 3):
        # Check signal[i:i+4]
        comparisons = [signal[i+j] == signal[i+k] for j in range(3) for k in range(j+1, 4)]
        if True not in comparisons:
            return i+4
    raise ValueError('No start-of-packet marker found')


def solve_part_two(signal) -> str:
    # Finds the start-of-message marker in the signal
    # Try to be more clever than the previous part
    signal_buffer = {i: 0 for i in range(97, 123)}
    for i in range(14):
        signal_buffer[ord(signal[i])] += 1

    for i in range(14, len(signal)):
        # Check if all elements are unique
        if max(signal_buffer.values()) > 1:
            # Add and remove chars from buffer
            signal_buffer[ord(signal[i])] += 1
            signal_buffer[ord(signal[i-14])] -= 1
        else:
            return i
    raise ValueError('No start-of-message marker found')

def main(signal: str):
    solution_1 = solve_part_one(signal)
    print(f'Solution to day 06, part 1: {solution_1}')

    solution_2 = solve_part_two(signal)
    print(f'Solution to day 06, part 2: {solution_2}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        parsed_file = load_file(sys.argv[1])
    else:
        parsed_file = load_file('problem06.in')

    main(parsed_file)

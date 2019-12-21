# https://adventofcode.com/2019/day/16
import numpy as np


def load_file(filename: str):
    first_input = list()
    with open(filename) as f:
        first_input = [int(i) for i in f.readline()[:-1]]
    return first_input


def c_div(a, b):
    return int(-(-a // b))


def main(fft_input):
    copy = [i for i in fft_input]
    # # base_pattern = np.array([0, 1, 0, -1])
    # num_phases = 100
    # for _ in range(num_phases):
    #     output = list()
    #     max_el = 0
    #     for i in range(len(fft_input)):
    #         pos_indices = list()
    #         neg_indices = list()
    #         for j in range(c_div(len(fft_input), 4 * (i + 1))):
    #             pos_indices += [
    #                 (4 * j + 1) * (i + 1) + k - 1 for k in range(i + 1)
    #                 if (4 * j + 1) * (i + 1) + k - 1 < len(fft_input)
    #             ]
    #             neg_indices += [
    #                 (4 * j + 3) * (i + 1) + k - 1 for k in range(i + 1)
    #                 if (4 * j + 3) * (i + 1) + k - 1 < len(fft_input)]
    #         raw_element = (sum([fft_input[j] for j in pos_indices])
    #                        - sum([fft_input[j] for j in neg_indices]))
    #         element = abs(raw_element) % 10
    #         output.append(element)
    #         if raw_element > max_el:
    #             max_el = raw_element
    #     fft_input = output
    # out_str = ''.join([str(i) for i in fft_input])
    # print(out_str[:8])

    # Part 2
    offset = sum([10**(6 - i) * copy[i] for i in range(7)])
    copy_length, signal_length = len(copy), len(copy) * 10**4
    assert offset / signal_length > 0.5
    signal_tail = [copy[i % copy_length] for i in range(offset, signal_length)]
    for _ in range(100):
        output = list()
        running_sum = 0
        for i in range(signal_length - offset):
            running_sum += signal_tail[signal_length - offset - i - 1]
            output.append(abs(running_sum) % 10)
        signal_tail = output[::-1]
    out_str = ''.join([str(i) for i in signal_tail])
    print(out_str[:8])



if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        problem_input = load_file(sys.argv[1])
    else:
        problem_input = load_file('problem16.in')

    main(problem_input)

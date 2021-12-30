# https://adventofcode.com/2021/day/8


def load_file(filename: str) -> list:
    """Load the list of crab positions from filename

    :param filename: Location of the input file
    :return: List of display entries
    """
    entries = list()
    with open(filename) as f:
        for line in f:
            entries.append(
                (line.split('|')[0].split(), line.split('|')[1].split())
            )
    return entries


def solve_part_one(entries: list) -> int:
    counter = 0
    for e in entries:
        for digit in e[1]:
            n = len(digit)
            if n in [2, 3, 4, 7]:
                counter += 1
    return counter
    

def solve_part_two(entries: list) -> int:
    sum = 0
    for e in entries:
        n = ''
        decoder = {len(m): set(m) for m in e[0]}
        for digit in e[1]:
            if len(digit) == 2:
                n += '1'
            elif len(digit) == 3:
                n += '7'
            elif len(digit) == 4:
                n += '4'
            elif len(digit) == 7:
                n += '8'
            elif len(digit) == 6 and decoder[4] <= set(digit):
                n += '9'
            elif len(digit) == 6 and decoder[2] <= set(digit):
                n += '0'
            elif len(digit) == 6:
                n += '6'
            elif len(digit) == 5 and decoder[2] <= set(digit):
                n += '3'
            elif len(digit) == 5 and len(decoder[4] & set(digit)) == 2:
                n += '2'
            elif len(digit) == 5 and len(decoder[4] & set(digit)) == 3:
                n += '5'
            else:
                raise ValueError('Unexpected value of digit')
        sum += int(n)
    return sum
                

def main(entries: list):
    solution_1 = solve_part_one(entries)
    print('Solution to day 08, part 1: {}'.format(solution_1))

    solution_2 = solve_part_two(entries)
    print('Solution to day 08, part 2: {}'.format(solution_2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        inputs = load_file(sys.argv[1])
    else:
        inputs = load_file('problem08.in')
    main(inputs)

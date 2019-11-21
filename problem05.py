# https://adventofcode.com/2018/day/5


def main(poly: str):
    new_poly = poly
    counter = 0
    while True:
        # This is slow
        for i in range(len(new_poly) - 1):
            if new_poly[i].swapcase() == new_poly[i+1]:
                new_poly = new_poly[:i] + new_poly[i+2:]
                counter += 1
                print('Reaction {}'.format(counter))
                break
        if i == len(new_poly) - 2:
            break
    print(len(new_poly))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        # Run test case
        filename = sys.argv[1]
    else:
        # Run problem
        filename = 'problem05.in'

    with open(filename) as f:
        polymer = f.readline()[:-1]

    main(polymer)

# https://adventofcode.com/2018/day/5


def collapse(poly):
    new_poly = poly
    while True:
        reactions = list()
        for i in range(len(new_poly) - 1):
            if new_poly[i].swapcase() == new_poly[i + 1]:
                # Flag places to react
                if len(reactions) == 0:
                    reactions.append(i)
                elif reactions[-1] + 1 != i:
                    reactions.append(i)

        if len(reactions) == 0:
            break

        temp_poly = new_poly[:reactions[0]]
        for j in range(1, len(reactions)):
            temp_poly += new_poly[reactions[j - 1] + 2:reactions[j]]

        if reactions[-1] < len(new_poly) - 2:
            temp_poly += new_poly[reactions[-1] + 2:]

        new_poly = temp_poly
    return new_poly


def remove_monomer(poly: str, monomer: str) -> str:
    new_poly = poly.replace(monomer, '')
    new_poly = new_poly.replace(monomer.upper(), '')
    return new_poly


def main(poly: str):
    monomers = set(poly.lower())
    new_poly = collapse(poly)
    print(len(new_poly))

    min_length = len(poly)
    min_monomer = ''
    for monomer in monomers:
        temp_poly = remove_monomer(poly, monomer)
        poly_length = len(collapse(temp_poly))
        if poly_length < min_length:
            min_length = poly_length
            min_monomer = monomer
    print(min_length, min_monomer)


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

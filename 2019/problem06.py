# https://adventofcode.com/2019/day/6


def load_file(filename: str) -> dict:
    with open(filename) as f:
        raw_orbits = f.readlines()

    orbits = dict()
    for line in raw_orbits:
        value, key = line[:-1].split(')')
        orbits[key] = value
    return orbits


def get_lineage(parent: str, orbits: dict) -> list:
    try:
        lineage = get_lineage(orbits[parent], orbits)
        lineage.append(parent)
        return lineage
    except KeyError:
        return [parent]


def main(orbits: dict):
    orbit_count = 0
    for child, parent in orbits.items():
        orbit_count += len(get_lineage(parent, orbits))
    print(orbit_count)

    my_lineage = get_lineage('YOU', orbits)
    santas_lineage = get_lineage('SAN', orbits)
    i = 0
    while my_lineage[i] == santas_lineage[i]:
        i += 1

    print(len(my_lineage) + len(santas_lineage) - 2 * (i + 1))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        orbits = load_file(sys.argv[1])
    else:
        orbits = load_file('problem06.in')

    main(orbits)

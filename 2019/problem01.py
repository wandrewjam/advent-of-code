# https://adventofcode.com/2019/day/1


def load_file(filename: str) -> list:
    """Load the module masses from  a file

    :param filename: Location of the input file
    :return: List of module masses
    """
    with open(filename) as f:
        masses = f.readlines()
    masses = [int(mass) for mass in masses]
    return masses


def calculate_fuel(mass: int, method: int = 1) -> int:
    """Calculate the fuel required for a single module

    :param mass: List of module masses
    :param method: Integer specifying whether to include the mass of the
    additional fuel in the calculation
    :return: Amount of fuel required
    """
    if method == 1:
        fuel = mass // 3 - 2
    elif method == 2:
        fuel = mass // 3 - 2
        additional_fuel = fuel // 3 - 2
        while additional_fuel > 0:
            fuel += additional_fuel
            additional_fuel = additional_fuel // 3 - 2
    else:
        raise ValueError('method is invalid')
    return fuel


def main(masses: list):
    total_fuel = sum([calculate_fuel(mass, method=1) for mass in masses])
    print('Solution to day 01, part 1: {}'.format(total_fuel))

    total_fuel = sum([calculate_fuel(mass, method=2) for mass in masses])
    print('Solution to day 01, part 2: {}'.format(total_fuel))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        raw_masses = load_file(sys.argv[1])
    else:
        raw_masses = load_file('problem01.in')

    main(raw_masses)

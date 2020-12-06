# https://adventofcode.com/2020/day/4


def load_file(filename: str):
    """Read and parse passport entries in file

    :param filename: Location of the file containing the passports
    :return: List of parsed passports
    """
    passport_list = []
    with open(filename, 'r') as f:
        lin = ''
        for line in f:
            if line == '\n':
                dummy = [tuple(l.split(':')) for l in lin.split()]
                passport_list.append(dict(dummy))
                lin = ''
            else:
                lin += line
        dummy = [tuple(l.split(':')) for l in lin.split()]
        passport_list.append(dict(dummy))
    return passport_list


def is_valid_passport(passport: dict):
    try:
        assert 1920 <= int(passport['byr']) <= 2002
        assert 2010 <= int(passport['iyr']) <= 2020
        assert 2020 <= int(passport['eyr']) <= 2030

        if passport['hgt'][-2:] == 'cm':
            assert 150 <= int(passport['hgt'][:-2]) <= 193
        elif passport['hgt'][-2:] == 'in':
            assert 59 <= int(passport['hgt'][:-2]) <= 76
        else:
            return False

        assert passport['hcl'][0] == '#'
        assert len(passport['hcl'][1:]) == 6
        assert set(passport['hcl'][1:]) <= {hex(i)[2:] for i in range(16)}

        assert passport['ecl'] in {'amb', 'blu', 'brn', 'gry',
                                   'grn', 'hzl', 'oth'}

        assert len(passport['pid']) == 9
        assert set(passport['pid']) <= {str(i) for i in range(10)}
    except (KeyError, AssertionError):
        return False

    return True


def main(passports: list):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    count = 0
    count2 = 0
    for pport in passports:
        count += required_keys <= pport.keys()
        count2 += is_valid_passport(pport)

    print('Solution to 2020 day 04, part 1: {}'.format(count))
    print('Solution to 2020 day 04, part 2: {}'.format(count2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        passport_list = load_file(sys.argv[1])
    else:
        passport_list = load_file('problem04.in')

    main(passport_list)

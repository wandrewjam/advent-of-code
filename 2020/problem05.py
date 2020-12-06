# https://adventofcode.com/2020/day/4


def load_file(filename: str) -> list:
    """Read file of seat locations

    :param filename: Location of seat input file
    :return: List of seat specification strings
    """
    with open(filename, 'r') as f:
        seats = f.readlines()
    seats = [seat[:-1] for seat in seats]
    return seats


def get_seat_id(seat_str: str) -> int:
    """Parse the seat specification string, and return the seat ID

    :param seat_str: Seat specification string
    :return: Seat ID
    """
    row = 0
    col = 0
    for i, char in enumerate(seat_str[:7]):
        row += (char == 'B') * 2 ** (6 - i)

    for i, char in enumerate(seat_str[7:]):
        col += (char == 'R') * 2 ** (2 - i)

    return row * 8 + col


def find_my_seat(seat_ids: list) -> int:
    """Find my seat from the list of seat IDs

    :param seat_ids: List of seat IDs
    :return: My seat ID
    """
    seat_ids.sort()
    for i, id in enumerate(seat_ids):
        if seat_ids[i+1] == id + 2:
            return id + 1


def main(seats: list):
    seat_ids = [get_seat_id(seat) for seat in seats]
    print('Solution to 2020 day 05, part 1: {}'.format(max(seat_ids)))

    my_seat = find_my_seat(seat_ids)
    print('Solution to 2020 day 05, part 2: {}'.format(my_seat))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        seat_list = load_file(sys.argv[1])
    else:
        seat_list = load_file('problem05.in')

    main(seat_list)

# https://adventofcode.com/2020/day/11


def load_seating(filename: str) -> list:
    """Load the seating arrangement from a file

    :param filename: Location of the seat arrangement file
    :return: List of seats
    """
    with open(filename, 'r') as f:
        lines = []
        for line in f:
            lines.append(list(line[:-1]))
    return lines


def array_equal(current_arr: list, new_arr: list) -> bool:
    """Test whether two seating arrangements are equal

    :param current_arr: Current seating arrangement
    :param new_arr: New seating arrangement
    :return: True if arrays are equal, False otherwise
    """
    for i in range(len(current_arr)):
        for j in range(len(current_arr[0])):
            if new_arr[i][j] != current_arr[i][j]:
                return False
    return True


def get_adjacent_seats(i: int, j: int, seat_arr: list, rule: int) -> list:
    """Get all seats adjacent to the current seat

    :param i: Row number of the current seat
    :param j: Column number of the current seat
    :param seat_arr: Current seating arrangement
    :param rule: 1 or 2 -- Use the part 1 or part 2 rule to update seats
    :return: Next seating arrangement
    """
    adjacent_seats = []
    for k1 in range(-1, 2):
        for k2 in range(-1, 2):
            if k1 == k2 == 0:
                continue
            factor = 1
            while True:
                if i + k1 * factor < 0 or j + k2 * factor < 0:
                    break
                try:
                    seat_to_add = seat_arr[i + k1 * factor][j + k2 * factor]
                except IndexError:
                    break
                if rule == 1:
                    adjacent_seats.append(seat_to_add)
                    break
                elif rule == 2:
                    factor += 1
                    if seat_to_add != '.':
                        adjacent_seats.append(seat_to_add)
                        break
    return adjacent_seats


def update_seating(seat_arr: list, rule: int) -> list:
    """Generate the next seating arrangement according to rule 1 or 2

    :param seat_arr: Seating arrangement
    :param rule: 1 or 2 -- Use the part 1 or part 2 rule to update seats
    :return: Next seating arrangement
    """
    new_arr = [[s for s in r] for r in seat_arr]
    if rule == 1:
        seat_threshold = 4
    elif rule == 2:
        seat_threshold = 5
    else:
        raise ValueError('rule is invalid')

    for i, row in enumerate(seat_arr):
        for j, seat in enumerate(row):
            adjacent_seats = get_adjacent_seats(i, j, seat_arr, rule)

            if seat == 'L' and '#' not in adjacent_seats:
                new_arr[i][j] = '#'
            elif seat == '#':
                if sum([s == '#' for s in adjacent_seats]) >= seat_threshold:
                    new_arr[i][j] = 'L'
    return new_arr


def find_stable_arrangement(seat_arr, rule):
    """Iterate the seating until reaching a stable arrangement

    :param seat_arr: Seating arrangement
    :param rule: 1 or 2 -- Use the part 1 or part 2 rule to update seats
    :return: Stable seating arrangement
    """
    current_arr = seat_arr.copy()
    while True:
        new_arr = update_seating(current_arr, rule)
        if array_equal(current_arr, new_arr):
            break
        current_arr = new_arr.copy()
    count = 0
    for row in current_arr:
        for seat in row:
            count += seat == '#'
    return count


def main(seat_arr: list):
    count1 = find_stable_arrangement(seat_arr, rule=1)
    print('Solution to 2020 day 11, part 1: {}'.format(count1))
    count2 = find_stable_arrangement(seat_arr, rule=2)
    print('Solution to 2020 day 11, part 2: {}'.format(count2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        seats = load_seating(sys.argv[1])
    else:
        seats = load_seating('problem11.in')

    main(seats)

# https://adventofcode.com/2020/day/13


def load_schedules(filename: str) -> tuple:
    with open(filename, 'r') as f:
        departure_time = int(f.readline())
        schedules = f.readline().split(',')
    return departure_time, schedules


def find_earliest_departure(departure_time, schedules):
    differences = {}
    for schedule in schedules:
        try:
            interval = int(schedule)
        except ValueError:
            continue
        differences[schedule] = interval - departure_time % interval
    min_bus = min(differences.keys(), key=lambda x: differences[x])
    min_diff = differences[min_bus]
    return min_bus, min_diff


def main(departure_time, schedules):
    min_bus, min_diff = find_earliest_departure(departure_time, schedules)
    print('Solution to 2020 day 13, part 1: {}'
          .format(int(min_bus) * min_diff))

    


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        time, bus_schedule = load_schedules(sys.argv[1])
    else:
        time, bus_schedule = load_schedules('problem13.in')

    main(time, bus_schedule)

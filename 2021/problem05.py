# https://adventofcode.com/2021/day/5


def load_file(filename: str) -> list:
    """Load the list of vent lines from filename

    :param filename: Location of the input file
    :return: List of vent lines
    """
    vents = []
    with open(filename) as f:
        for line in f:
            start_str, finish_str = line.split('->')
            start = Point(*[int(s.strip()) for s in start_str.split(',')])
            finish = Point(*[int(s.strip()) for s in finish_str.split(',')])
            vents.append(VentLine(start, finish))
    return vents


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
        

class VentLine:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        xdiff = end.x - start.x
        ydiff = end.y - start.y

        self.points = set()
        if start.x < end.x:
            for ix in range(start.x, end.x + 1):
                if (ydiff * (ix - start.x)) % xdiff == 0:
                    iy = ydiff * (ix - start.x) // xdiff + start.y
                    self.points.add(Point(ix, iy))
        elif start.x > end.x:
            for ix in range(end.x, start.x + 1):
                if (ydiff * (ix - start.x)) % xdiff == 0:
                    iy = ydiff * (ix - start.x) // xdiff + start.y
                    self.points.add(Point(ix, iy))
        elif start.y < end.y:
            for iy in range(start.y, end.y + 1):
                if (xdiff * (iy - start.y)) % ydiff == 0:
                    ix = xdiff * (iy - start.y) // ydiff + start.x
                    self.points.add(Point(ix, iy))
        elif start.y > end.y:
            for iy in range(end.y, start.y + 1):
                if (xdiff * (iy - start.y)) % ydiff == 0:
                    ix = xdiff * (iy - start.y) // ydiff + start.x
                    self.points.add(Point(ix, iy))

    
def solve_part_one(vents: list) -> int:
    vent_counts = {}
    for vent in vents:
        if (vent.end.x - vent.start.x) * (vent.end.y - vent.start.y) == 0:
            for point in vent.points:
                try:
                    vent_counts[point] += 1
                except KeyError:
                    vent_counts[point] = 1

    count = len([val for val in vent_counts.values() if val >= 2])
    return count
                

def solve_part_two(vents: list) -> int:
    vent_counts = {}
    for vent in vents:
        for point in vent.points:
            try:
                vent_counts[point] += 1
            except KeyError:
                vent_counts[point] = 1

    count = len([val for val in vent_counts.values() if val >= 2])
    return count    


def main(vents: list):
    solution_1 = solve_part_one(vents)
    print('Solution to day 05, part 1: {}'.format(solution_1))

    solution_2 = solve_part_two(vents)
    print('Solution to day 05, part 2: {}'.format(solution_2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        inputs = load_file(sys.argv[1])
    else:
        inputs = load_file('problem05.in')
    main(inputs)

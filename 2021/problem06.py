# https://adventofcode.com/2021/day/6


def load_file(filename: str) -> list:
    """Load the list of lanternfish from filename

    :param filename: Location of the input file
    :return: List of lanternfish
    """
    with open(filename) as f:
        fish = [int(n) for n in f.readline().split(',')]
    return fish


def solve_part_one(fish: list) -> int:
    PERIOD = 80
    fish_copy = [f for f in fish]
    for _ in range(PERIOD):
        new_fish = list()
        for i in range(len(fish_copy)):
            if fish_copy[i] > 0:
                fish_copy[i] -= 1
            elif fish_copy[i] == 0:
                fish_copy[i] = 6
                new_fish.append(8)
            else:
                raise ValueError('fish timer must be non-negative')
        fish_copy += new_fish
    return len(fish_copy)
            
                

def solve_part_two(fish: list) -> int:
    PERIOD = 256
    new_fish = [0] * 9
    for f in fish:
        new_fish[f] += 1
        
    for _ in range(PERIOD):
        old_fish = [n for n in new_fish]
        new_fish = [0] * 9
        for i in range(len(old_fish)):
            if i == 0:
                new_fish[8] = old_fish[0]
                new_fish[6] = old_fish[0]
            elif i > 0:
                new_fish[i-1] += old_fish[i]
            else:
                raise ValueError('fish timer must be non-negative')
    return sum(new_fish)


def main(fish: list):
    solution_1 = solve_part_one(fish)
    print('Solution to day 06, part 1: {}'.format(solution_1))

    solution_2 = solve_part_two(fish)
    print('Solution to day 06, part 2: {}'.format(solution_2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        inputs = load_file(sys.argv[1])
    else:
        inputs = load_file('problem06.in')
    main(inputs)

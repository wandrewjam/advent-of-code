# https://adventofcode.com/2019/day/12
from math import gcd
from multiprocessing import Pool


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def get_total_energy(moons, t_steps=1000):
    num_moons = len(moons)
    velocities = [[0, 0, 0] for _ in range(num_moons)]
    for t in range(t_steps):
        for i, moon in enumerate(moons):
            for other_moon in moons:
                for j in range(3):
                    if moon[j] > other_moon[j]:
                        velocities[i][j] -= 1
                    elif moon[j] < other_moon[j]:
                        velocities[i][j] += 1
        moons = [[p + v for p, v in zip(moon, vel)]
                 for moon, vel in zip(moons, velocities)]
    potential_energy = [sum([abs(p) for p in moon]) for moon in moons]
    kinetic_energy = [sum([abs(v) for v in vel]) for vel in velocities]
    total_energy = sum([pe * ke for pe, ke
                        in zip(potential_energy, kinetic_energy)])
    return total_energy


def find_period(positions: tuple) -> int:
    velocities = (0,) * len(positions)
    i = 0
    past_configs = {(positions, velocities): i}
    while True and len(past_configs) < 1000000:
        new_position = tuple()
        new_velocity = tuple()
        for p, v in zip(positions, velocities):
            for p1 in positions:
                if p > p1:
                    v -= 1
                elif p < p1:
                    v += 1
            new_position += (p + v,)
            new_velocity += (v,)
        positions, velocities = new_position, new_velocity
        # if (positions, velocities) in past_configs:
        #     i = past_configs.index((positions, velocities))
        #     return len(past_configs) - i
        # past_configs.append((positions, velocities))
        try:
            i_past = past_configs[(positions, velocities)]
            return len(past_configs) - i_past
        except KeyError:
            i += 1
            past_configs[(positions, velocities)] = i
    return -1


def main(moons: list):
    total_energy = get_total_energy(moons)
    print(total_energy)

    periods = list()
    for i in range(3):
        periods.append(find_period(positions=tuple(zip(*moons))[i]))
    # pool = Pool(processes=3)
    # res = [pool.apply_async(find_period, args=(el,))
    #        for el in zip(*moons)]
    # periods = [r.get() for r in res]

    print(periods)
    print(lcm(lcm(periods[0], periods[1]), periods[2]))


def slow_period_find(moons):
    num_moons = len(moons)
    velocities = [[0, 0, 0] for _ in range(num_moons)]
    t_steps = 0
    past_positions = list([[p for p in moon] for moon in moons])
    past_velocities = list([[v for v in vels] for vels in velocities])
    while True:
        for i, moon in enumerate(moons):
            for other_moon in moons:
                for j in range(3):
                    if moon[j] > other_moon[j]:
                        velocities[i][j] -= 1
                    elif moon[j] < other_moon[j]:
                        velocities[i][j] += 1
        moons = [[p + v for p, v in zip(moon, vel)]
                 for moon, vel in zip(moons, velocities)]
        if (moons, velocities) in zip(past_positions, past_velocities):
            break
        t_steps += 1
        past_velocities.append([[v for v in vels] for vels in velocities])
        past_positions.append([[p for p in moon] for moon in moons])
    return t_steps


if __name__ == '__main__':
    starting_positions = [
        (-5, 6, -11), (-8, -4, -2), (1, 16, 4), (11, 11, -4)
    ]

    # starting_positions = [
    #     (-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)
    # ]

    # starting_positions = [
    #     (-8, -10, 0), (5, 5, 10), (2, -7, 3), (9, -8, -3)
    # ]

    main(starting_positions)

# https://adventofcode.com/2019/day/14


def load_file(filename: str):
    reactions = list()
    with open(filename) as f:
        for line in f:
            reactants_str, product_str = line.split('=>')
            product = {product_str.split()[1]: int(product_str.split()[0])}
            reactants = dict()
            for reactant in reactants_str.split(','):
                reactants[reactant.split()[1]] = int(reactant.split()[0])
            reactions.append((reactants, product))
    return reactions


def c_div(a, b):
    return -(-a // b)


def chemicals_required(reactions, chemical, target, leftovers):
    ore_count = 0
    for (i, rxn) in enumerate(reactions):
        if chemical in rxn[1]:
            assert chemical != 'ORE'
            produced = rxn[1][chemical]
            reaction_firings = c_div(target, produced)
            try:
                leftovers[chemical] = produced * reaction_firings - target
            except KeyError:
                assert chemical == 'FUEL'
                pass

            for reactant, required in reactions[i][0].items():
                try:
                    leftover = leftovers[reactant]
                    new_target = reaction_firings * required - leftover
                    if new_target < 0:
                        leftovers[reactant] = -new_target
                except KeyError:
                    leftovers[reactant] = 0
                    leftover = leftovers[reactant]
                    new_target = reaction_firings * required - leftover
                ore_count += chemicals_required(
                    reactions, reactant, new_target,
                    leftovers
                )
            return ore_count
    assert chemical == 'ORE'
    return target


def ore_required(reactions, leaf_count) -> int:
    ore = 0
    for (i, rxn) in enumerate(reactions):
        if 'ORE' in rxn[0]:
            for chemical in rxn[1]:
                target = leaf_count[chemical]
                produced = rxn[1][chemical]
                reaction_firings = c_div(target, produced)
                ore += reaction_firings * rxn[0]['ORE']
    return ore


def main(reactions: list):
    for (i, rxn) in enumerate(reactions):
        if 'FUEL' in rxn[1].keys():
            i_parent = i
            break
    print(reactions[i_parent][0].items())
    print(len(reactions))
    print(reactions)
    leftovers = {}
    ore_per_fuel = chemicals_required(reactions, 'FUEL', 1, leftovers)
    print(ore_per_fuel)
    print(leftovers)

    leftovers = {}
    total_ore = 10**12
    fuel_counter = 0
    while True:
        increment = total_ore // ore_per_fuel
        if increment < 1:
            break
        # increment = 1
        total_ore -= chemicals_required(reactions, 'FUEL', increment, leftovers)
        # if total_ore < 0:
        #     break
        fuel_counter += increment
    print(fuel_counter)
    # ore = ore_required(reactions, leaf_count)
    # print(leaf_count)
    # print(leftovers)
    # print(ore)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        reactions = load_file(sys.argv[1])
    else:
        reactions = load_file('problem14.in')

    main(reactions)

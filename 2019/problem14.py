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


def main(reactions: list):
    for (i, rxn) in enumerate(reactions):
        if 'FUEL' in rxn[1].keys():
            i_parent = i
            break
    print(reactions[i_parent][0].keys())
    print(len(reactions))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        reactions = load_file(sys.argv[1])
    else:
        reactions = load_file('problem14_test1.in')

    main(reactions)

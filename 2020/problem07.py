# https://adventofcode.com/2020/day/7


class Tree:
    def __init__(self, root):
        self.root = root


class Node:
    def __init__(self, name, parent, left_child, right_sibling):
        self.name = name
        self.parent = parent
        self.child = left_child
        self.sibling = right_sibling


def load_file(filename: str) -> list:
    """Read file containing the bag-containing specifications

    :param filename: Location of the bag-spec file
    :return: List of bag-containing restrictions
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line[:-1] for line in lines]
    return lines


def parse_bags(bag_restrictions: list) -> list:
    """Parse the list of raw bag restrictions given by the input file

    :param bag_restrictions: List of raw bag restrictions
    :return: Parsed bag restrictions
    """
    parsed_restrictions = []
    for line in bag_restrictions:
        parent_str, children_str = line.split(' contain ')
        parent_str = parent_str[:-5]
        children_list = children_str.split(', ')
        children_list = [child.split(' bag')[0] for child in children_list]
        if children_list[0] == 'no other':
            children_list = []
        else:
            children_list = [child.split(' ', maxsplit=1)
                             for child in children_list]
        parsed_restrictions.append((parent_str, children_list))
    return parsed_restrictions


def find_containing_bags(bag, parsed_restrictions):
    containers = set()
    for parent, children in parsed_restrictions:
        for child in children:
            if bag == child[1]:
                containers = set.union(
                    find_containing_bags(parent, parsed_restrictions),
                    {parent}, containers)
    return containers


def count_bags_contained(bag, parsed_restrictions):
    count = 0
    for parent, children in parsed_restrictions:
        if bag == parent:
            for child in children:
                count += (count_bags_contained(child[1], parsed_restrictions)
                          * int(child[0]))
    return count + 1


def main(bag_data):
    parsed_restrictions = parse_bags(bag_data)
    my_bag = 'shiny gold'
    containers = find_containing_bags(my_bag, parsed_restrictions)
    print(len(containers))

    bags_contained = count_bags_contained(my_bag, parsed_restrictions) - 1
    print(bags_contained)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        bags = load_file(sys.argv[1])
    else:
        bags = load_file('problem07.in')

    main(bags)

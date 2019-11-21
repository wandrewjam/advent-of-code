# https://adventofcode.com/2018/day/3


def load_file(file) -> list:
    """
    Read a file containing a list of rectangle definitions, and return
        a list with the rectangle specs. The ID is the array location.
    :param file: Text file containing a rectangle definition on each
        line
    :return: List with parsed rectangle definition
    """
    import re
    rectangles = list()
    with open(file) as f:
        for line in f:
            rectangles.append(re.split('\D+', line)[1:-1])

    for i in range(len(rectangles)):
        for j in range(len(rectangles[i])):
            rectangles[i][j] = int(rectangles[i][j])
    return rectangles


def make_claims(rectangles: list, side: int) -> list:
    """
    Place all claims by ID on each square inch of fabric
    :param rectangles: a Python list of claims
    :param side: the side length of the square of fabric
    :return: a list of lists of lists. The innermost list contains all
        claim IDs made to specific square inch of fabric. The 2
        outermost lists give the location of the square inch.
    """
    cloth = [[list() for _ in range(side)] for _ in range(side)]
    for rectangle in rectangles:
        id = rectangle[0]
        for i in range(rectangle[-2]):
            for j in range(rectangle[-1]):
                cloth[rectangle[1] + i][rectangle[2] + j].append(id)

    return cloth


def calculate_overlap_area(cloth: list) -> int:
    """
    Calculate the total area of overlapping claims
    :param cloth:  List of claims made on each square inch of the cloth
    :return: Area of overlapping claims
    """
    area = 0
    for row in cloth:
        for col in row:
            area += (len(col) >= 2)

    return area


def extract_claim_list(rectangles: list) -> list:
    """
    Generate a list of all the claim IDs
    :param rectangles: List of claims
    :return: List of all the claim IDs
    """
    id_list = list()
    for rectangle in rectangles:
        id_list.append(rectangle[0])
    return id_list


def find_intact_claim(cloth: list, id_list: list) -> int:
    """
    Find the ID of the intact claim

    This method assumes that there is exactly one intact claim.

    :param cloth: List of claims made on each square inch of the cloth
    :param id_list: List of all the claim IDs
    :return: ID of the intact claim
    """
    claim_intact = [True for _ in range(max(id_list))]
    for row in cloth:
        for col in row:
            if len(col) >= 2:
                for id in col:
                    claim_intact[id-1] = False

    for (id, id_intact) in enumerate(claim_intact):
        if id_intact:
            return id+1


def main(rectangles: list, side_length: int):
    cloth = make_claims(rectangles, side_length)
    overlap_area = calculate_overlap_area(cloth)
    id_list = extract_claim_list(rectangles)
    intact_claim = find_intact_claim(cloth, id_list)
    print(overlap_area)
    print(intact_claim)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        rectangles = load_file(sys.argv[1])
        side_length = int(sys.argv[2])
    else:
        rectangles = load_file('problem03.in')
        side_length = 1000

    main(rectangles, side_length)

# https://adventofcode.com/2022/day/2


def load_file(filename: str) -> list:
    """Load rock, paper, scissors strategy guide

    :param filename: Location of the input file
    :return: List of opponent plays and responses
    """
    with open(filename) as f:
        games = f.readlines()
    games = [game.split() for game in games]
    return games


def solve_part_one(games: list) -> int:
    score = 0
    for game in games:
        # Converts character encoding for rock, paper, or scissors
        # to a numerical encoding: 0 - rock, 1 - paper, 2 - scissors
        opponent_play = ord(game[0]) - 65
        your_play = ord(game[1]) - 88
        score += your_play + 1
        # Outcome is encoded as: 0 - draw, 1 - you win, 2 - you lose
        outcome = (your_play - opponent_play) % 3
        if outcome == 0:  # Draw
            score += 3
        elif outcome == 1:  # You win
            score += 6
    return score


def solve_part_two(games: list) -> int:
    # Play and outcome encodings are the same as in solve_part_one
    score = 0
    for game in games:
        opponent_play = ord(game[0]) - 65
        outcome = (ord(game[1]) - 89) % 3
        your_play = (opponent_play + outcome) % 3
        score += your_play + 1
        if outcome == 0:  # Draw
            score += 3
        elif outcome == 1:  # You win
            score += 6
    return score

def main(games: list):
    solution_1 = solve_part_one(games)
    print(f'Solution to day 02, part 1: {solution_1}')

    solution_2 = solve_part_two(games)
    print(f'Solution to day 02, part 2: {solution_2}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        parsed_file = load_file(sys.argv[1])
    else:
        parsed_file = load_file('problem02.in')

    main(parsed_file)

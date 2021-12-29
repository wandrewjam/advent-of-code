# https://adventofcode.com/2021/day/4


def load_file(filename: str) -> tuple:
    """Load the bingo input and cards from filename

    :param filename: Location of the input file
    :return: Bingo input, and a list of bingo cards
    """
    bingo_cards = []
    with open(filename) as f:
        draw = [int(n) for n in f.readline().split(',')]
        current_card = []
        for line in f:
            if line == '\n' and len(current_card) > 0:
                bingo_cards.append(BingoCard(board=current_card))
                current_card = []
            elif line != '\n':
                current_card.append([int(n) for n in line.split()])
        bingo_cards.append(BingoCard(board=current_card))
    return draw, bingo_cards


class BingoCard:
    """Define a BingoCard class for updating boards and checking wins"""
    def __init__(self, board: list):
        self.board = board
        self.marks = []
        self.win = False

    def add_mark(self, num: int):
        self.marks.append(num)
        return self._check_win()

    def _check_win(self):
        side = 5
        for row in self.board:
            row_marked = len([e for e in row if e in self.marks])
            if row_marked == side:
                return True
        for j in range(side):
            col_marked = len([self.board[i][j] for i in range(side)
                              if self.board[i][j] in self.marks])
            if col_marked == side:
                return True
        return False


def solve_part_one(draw: list, bingo_cards: list) -> int:
    for n in draw:
        for c in bingo_cards:
            game_won = c.add_mark(n)
            if game_won:
                sum_unmarked = sum([n for row in c.board for n in row if n not in c.marks])
                return sum_unmarked * n


def solve_part_two(draw: list, bingo_cards: list) -> int:
    total_boards = len(bingo_cards)
    wins = []
    for n in draw:
        for (i, c) in enumerate(bingo_cards):
            if i not in wins:
                game_won = c.add_mark(n)
                if game_won:
                    wins.append(i)
                    if len(wins) == total_boards:
                        sum_unmarked = sum([n for row in c.board for n in row
                                            if n not in c.marks])
                        return sum_unmarked * n                        


def main(draw: list, bingo_cards: list):
    solution_1 = solve_part_one(draw, bingo_cards)
    print('Solution to day 04, part 1: {}'.format(solution_1))

    solution_2 = solve_part_two(draw, bingo_cards)
    print('Solution to day 04, part 2: {}'.format(solution_2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        inputs = load_file(sys.argv[1])
    else:
        inputs = load_file('problem04.in')
    main(*inputs)

# https://adventofcode.com/2018/day/18


def count_adjacent(area, row, col, id, nrows, ncols):
    count = 0
    for i in range(-1, 2):
        if 0 <= row + i < nrows:
            for j in range(-1, 2):
                if 0 <= col + j < ncols:
                    if not (i == 0 and j == 0):
                        count += (area[row+i][col+j] == id)

    return count


if __name__ == '__main__':
    import sys

    area = list()
    with open('problem18_test.in') as f:
        for line in f:
            area.append(list(line))

    nrows = len(area)
    ncols = len(area[0])
    for row in range(nrows):
        for col in range(ncols):
            if area[row][col] == '.':
                trees = count_adjacent(area, row, col, '|', nrows, ncols)
                if trees >= 3:
                    area[row][col] = '|'
            elif area[row][col] == '|':
                yards = count_adjacent(area, row, col, '#', nrows, ncols)
                if yards >= 3:
                    area[row][col] = '#'
            elif area[row][col] == '#':
                yards = count_adjacent(area, row, col, '#', nrows, ncols)
                trees = count_adjacent(area, row, col, '|', nrows, ncols)
                if yards == 0 or trees == 0:
                    area[row][col] = '.'

    for row in range(nrows):
        area[row] = ''.join(area[row])

    print(area)

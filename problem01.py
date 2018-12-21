# https://adventofcode.com/2018/day/1

if __name__ == '__main__':
    with open('problem01_test.in') as f:
        sequence = f.read()

    sequence = sequence.split(', ')
    frequency = 0
    for i in range(len(sequence)):
        frequency += int(sequence[i])

    print('Frequency is ', frequency)

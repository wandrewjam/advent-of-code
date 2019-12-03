# https://adventofcode.com/2018/day/7


def load_file(filename: str) -> list:
    with open(filename) as f:
        rules_raw = f.readlines()
    rules = [(rule[5], rule[36]) for rule in rules_raw]
    return rules


def main(rules: list):
    sequence = ''

    for rule in rules:
        if len(sequence) == 0:
            sequence = ''.join(rule)
        else:
            for (j, char) in enumerate(sequence):
                if char == rule[0]:
                    sequence = sequence[:j] + rule[1] + sequence[j:]
                    continue
                if char > sequence[j+1]:
                    sequence = sequence[:j] + sequence[j+2:j:-1] + sequence[j+2]
    print(sequence)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        rules_list = load_file(sys.argv[1])
    else:
        rules_list = load_file('problem07_test.in')

    main(rules_list)

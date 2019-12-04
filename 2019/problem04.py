# https://adventofcode.com/2019/day/4


def is_valid_password(i: int, version: int = 1) -> bool:
    i_digits = [int(digit) for digit in str(i)]
    is_increasing, repeats = True, False
    for k in range(len(i_digits) - 1):
        if i_digits[k] > i_digits[k+1]:
            is_increasing = False
        elif version == 1 and i_digits[k] == i_digits[k+1]:
            repeats = True
        elif version == 2 and i_digits[k] == i_digits[k+1]:
            if 0 < k < len(i_digits) - 2:
                valid_repeat = ((i_digits[k-1] != i_digits[k])
                                and (i_digits[k+1] != i_digits[k+2]))
            elif k == 0:
                valid_repeat = i_digits[k+1] != i_digits[k+2]
            elif k == len(i_digits) - 2:
                valid_repeat = i_digits[k-1] != i_digits[k]
            else:
                raise ValueError('k takes on an unexpected value')
            if valid_repeat:
                repeats = True

    return is_increasing and repeats


def main(code_range: iter):
    password_count = [0, 0]
    for i in code_range:
        password_count[0] += int(is_valid_password(i, version=1))
        password_count[1] += int(is_valid_password(i, version=2))

    print(password_count[0])
    print(password_count[1])


if __name__ == '__main__':
    possible_range = range(156218, 652527 + 1)

    main(possible_range)

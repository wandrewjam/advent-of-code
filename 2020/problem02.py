# https://adventofcode.com/2020/day/2


def load_file(filename: str) -> list:
    """Load the passwords and policies from a file

    :param filename: Location of the input file
    :return: List of passwords and policies
    """
    with open(filename) as f:
        entries = f.readlines()
    entries = [parse_line(e) for e in entries]
    return entries


def parse_line(line: str) -> tuple:
    """Parse one line of the password file

    :param line: Line of the password file
    :return: Tuple of the password policy and password
    """
    policy_str, password = line.split(': ')

    # Parse the policy definition
    policy_chr = policy_str.split()[1]
    policy_min, policy_max = [int(s) for s in policy_str.split()[0].split('-')]
    policy = PasswordPolicy(policy_chr, policy_min, policy_max)
    return policy, password


class PasswordPolicy:
    def __init__(self, char, min, max):
        """Instantiate a new password policy

        :param char: Character restricted by the password policy
        :param min: Minimum allowed number of "char"s
        :param max: Maximum allowed number of "char"s
        """
        self.char = char
        self.min = min
        self.max = max

    def is_valid(self, password: str, old_policy: bool = True) -> bool:
        """Check if a password is valid under the current policy

        :param password: String of the password to check
        :param old_policy: Boolean for whether to use the old policy
        :return: Boolean for whether the password is valid
        """
        if old_policy:
            appearances = password.count(self.char)
            return self.min <= appearances <= self.max
        else:
            return ((password[self.min-1] == self.char)
                    ^ (password[self.max-1] == self.char))


def main(data: list):
    valid_list = [policy.is_valid(pwd) for policy, pwd in data]
    print('Solution to 2020 day 02, part 1: {}'.format(sum(valid_list)))

    valid_list2 = [policy.is_valid(pwd, old_policy=False)
                   for policy, pwd in data]
    print('Solution to 2020 day 02, part 2: {}'.format(sum(valid_list2)))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        password_data = load_file(sys.argv[1])
    else:
        password_data = load_file('problem02.in')

    main(password_data)

# https://adventofcode.com/2018/day/4


def load_file(file: str) -> list:
    """
    Read a file containing an unsorted list of guard activities
    :param file: Text file containing guard activities
    :return: List of parsed and sorted guard activity information
    """
    activity_list = list()
    with open(file) as f:
        for line in f:
            raw_time = line[:18]
            raw_flag = line[19:-1]
            timestamp = datetime.datetime.strptime(raw_time,
                                                   '[%Y-%m-%d %H:%M]')
            if raw_flag == 'falls asleep':
                flag = 0
            elif raw_flag == 'wakes up':
                flag = 1
            else:
                flag = int(raw_flag.split()[1][1:])

            activity_list.append((timestamp, flag))

    activity_list.sort(key=lambda log: log[0])
    return activity_list


def parse_activity_list(activity_list: list) -> list:
    """

    :param activity_list:
    :return:
    """
    parsed_log = list()
    asleep = [False for _ in range(60)]
    for log in activity_list:
        if log[1] > 1:
            try:
                parsed_log.append((date, guard_id, asleep))
            except NameError:
                pass
            date = log[0].date()
            guard_id = log[1]
            asleep = [False for _ in range(60)]
        elif log[1] == 0:
            sleep_time = log[0].time().minute
            asleep[sleep_time:] = [True for _ in range(60 - sleep_time)]
        elif log[1] == 1:
            wake_time = log[0].time().minute
            asleep[wake_time:] = [False for _ in range(60 - wake_time)]
    parsed_log.append((date, guard_id, asleep))

    return parsed_log


def sleepiest_guard(daily_logs: list) -> int:
    """

    :param daily_logs:
    :return:
    """
    sleep_log = dict()
    for log in daily_logs:
        guard_id = str(log[1])
        sleep_minutes = sum(log[2])
        try:
            sleep_log[guard_id] += sleep_minutes
        except KeyError:
            sleep_log[guard_id] = sleep_minutes

    max_minutes = max(sleep_log.values())
    for key, value in sleep_log.items():
        if value == max_minutes:
            return int(key)


def sleepiest_minute(daily_logs: list, guard_id: int) -> tuple:
    """

    :param daily_logs:
    :param guard_id:
    :return:
    """
    minutes_total = [0 for _ in range(60)]
    for log in daily_logs:
        if log[1] == guard_id:
            for i in range(len(log[2])):
                minutes_total[i] += log[2][i]
    max_minutes = max(minutes_total)
    for (i, val) in enumerate(minutes_total):
        if val == max_minutes:
            return i, val


def part_one(daily_logs: list):
    guard_id = sleepiest_guard(daily_logs)
    minute = sleepiest_minute(daily_logs, guard_id)[0]
    print('The sleepiest guard is {}, and the sleepiest minute is {}'
          .format(guard_id, minute))
    print('The product of the two is: {}'.format(guard_id * minute))


def get_guard_ids(daily_logs: list) -> frozenset:
    guard_ids = set()
    for log in daily_logs:
        guard_ids.add(log[1])
    return frozenset(guard_ids)


def part_two(daily_logs):
    guard_ids = get_guard_ids(daily_logs)
    max_id = None
    max_minute = None
    max_sleeps = 0
    for id in guard_ids:
        minute, sleeps = sleepiest_minute(daily_logs, id)
        if sleeps > max_sleeps:
            max_sleeps = sleeps
            max_minute = minute
            max_id = id
    print('The solution to part two is : {}'.format(max_id * max_minute))


def main(table: list):
    """

    :param table: List of parsed guard activity information
    :return: None
    """
    daily_logs = parse_activity_list(table)
    part_one(daily_logs)
    part_two(daily_logs)


if __name__ == '__main__':
    import datetime
    import sys

    if len(sys.argv) > 1:
        # Run test case
        raw_table = load_file(sys.argv[1])
    else:
        # Run problem
        raw_table = load_file('problem04.in')

    main(raw_table)

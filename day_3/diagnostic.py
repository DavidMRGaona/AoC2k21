#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_report(case):
    with open(f'{case}') as f:
        report = f.read().splitlines()
    return report


# Part 1
def check_consumption(report):
    n = len(report)  # rows
    m = len(report[0])  # cols
    count = [0] * m

    for word in report:
        for i, b in enumerate(word):
            count[i] += int(b)

    gamma = ''.join(['1' if c > n / 2 else '0' for c in count])
    epsilon = ''.join(['0' if c > n / 2 else '1' for c in count])  # epsilon = ~gamma
    return int(epsilon, 2) * int(gamma, 2)


print('Part 1.', end=' ')
report = read_report('input')
chk = check_consumption(report)
print('Done!')
print(f'Consumption: {chk}')


# Part 2
def count_ones(report, idx):
    count = 0
    for word in report:
        count += int(word[idx])
    return count


## oxygen
def check_oxygen(report, i):
    # Recursive because why not
    if len(report) == 1:
        return report[0]

    count = count_ones(report, i)
    n = len(report)

    b = '1' if count >= n / 2 else '0'
    report = list(filter(lambda x: x[i] == b, report))
    # print(i, b, count, n)
    return check_oxygen(report, i + 1)


## co2
def check_co2(report, i):
    # The same as above because no time :_
    if len(report) == 1:
        return report[0]

    count = count_ones(report, i)
    n = len(report)

    b = '0' if count >= n / 2 else '1'
    report = list(filter(lambda x: x[i] == b, report))
    # print(i, b, count, n)
    return check_co2(report, i + 1)


print('Part 2...', end=' ')
report = read_report('input')
oxygen = check_oxygen(report, 0)
report = read_report('input')
co2 = check_co2(report, 0)
chk = int(oxygen, 2) * int(co2, 2)
print('Done!')
print(f'Life Support: {chk}')


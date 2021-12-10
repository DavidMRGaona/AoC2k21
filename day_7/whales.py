#!/usr/bin/env python
# -*- coding: utf-8 -*-

def scan_crabs(case):
    with open(f'{case}') as f:
        crabs = [int(x) for x in f.readline().split(',')]
    return crabs


# Part 1
def calculate_fuel(i, crabs):
    """ Calculates fuel consumption of every crab moving to 'i' position. Constant consumption """
    return sum([abs(crab - i) for crab in crabs])


def arrange_crabs(case):
    """ I suppose that the cheapest move is to go to the middle of the pack, the median. """
    crabs = scan_crabs(case)
    m = sorted(crabs)
    n = len(crabs)
    start = m[n // 2]
    return calculate_fuel(start, crabs)


print('Part 1...', end=' ')
print('Done!')
print(f'Total fuel consumption: {arrange_crabs("input")}')


# Part 2
def calculate_fuel(i, crabs):
    """ Calculates fuel consumption of every crab moving to 'i' position. Variable consumption """
    f = lambda x: sum(range(x + 1))
    return sum([f(abs(crab - i)) for crab in crabs])


def arrange_crabs(case):
    """
        Median is not the cheapest position anymore, but it is a good starting point.
        Just keep looking in the direction that minimizes the objective.
        Which I suppose that will be to the right (positions are limited at 0, so the values that will
        generate tons of fuel consumption are goint to be the big ones)
        There should be just one minimum, the optimal one.
    """
    crabs = scan_crabs(case)
    m = sorted(crabs)
    n = len(crabs)
    start = m[n // 2]
    fuel = calculate_fuel(start, crabs)

    next_ = start + 1
    next_fuel = calculate_fuel(next_, crabs)

    while (next_fuel < fuel):
        next_ += 1
        fuel = next_fuel
        next_fuel = calculate_fuel(next_, crabs)

    return fuel


print('Part 2...', end=' ')
fuel = arrange_crabs('input')
print('Done!')
print(f'Total fuel consumption: {fuel}')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def scan(case):
    with open(f'{case}', 'r') as f:
        return [int(x) for x in f.read().splitlines()]


def measure(data, i, w):
    """
    Read the sliding window from the sonar data and return its sum
    param: data. The sonar data (list of ints)
    param: i. Pointer's index
    param: w. Window's size
    return: Measure
    """
    return sum(data[i:(i+w)])


def evaluate(depths, w, offset):
    """
    Counts how many times a depth measure increases from previous one.
    param: depths. Sonar data (list of ints)
    param: w. Window's size
    param: offset: Separation between one measure and the next
    return: number of increasing measures
    """
    n = len(depths)
    larger = sum([measure(depths, i, w) < measure(depths, i + offset, w) for i in range(n - w)])
    return larger


# Part 1
print('Part 1...', end=' ')
depths = scan('input')
ev = evaluate(depths, 1, 1)
print(f'Done!')
print(f'Found {ev} increasing measurements.')


# Part 2
print('Part 2...', end=' ')
depths = scan('input')
ev = evaluate(depths, 3, 1)
print(f'Done!')
print(f'Found {ev} increasing measurements.')

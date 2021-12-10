#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_lantern_pop(case):
    with open(f'{case}', 'r') as f:
        lanterns = f.readline()

    return [int(x) for x in lanterns.split(',')]


def create_register(lanternfishes):
    # Register is a list where every position keeps track of the number of lanternfishes on every cycle
    # register[0] -> number of fishes on cycle 0, etc.
    register = [0] * 9
    for fish in lanternfishes:
        register[fish] += 1

    return register


def shift(register):
    # Shifts every position (fishes on cycle 1 -> cycle 0)
    # Fishes in cycle 0 spawn new fishes at cycle 8 and "move" themselves to cycle 6
    spawn = register[0]
    for i in range(len(register)-1):
        register[i] = register[i+1]
    register[6] += spawn
    register[8] = spawn

    return register


def simulate(register, days):
    for _ in range(days):
        register = shift(register)

    return sum(register)


# Part 1
print('Part 1.', end=' ')
lanternfishes = read_lantern_pop('input')
register = create_register(lanternfishes)
print(simulate(register, 80))
print('Done!')


# Part 2
print('Part 2.', end=' ')
lanternfishes = read_lantern_pop('input')
register = create_register(lanternfishes)
print(simulate(register, 256))
print('Done!')
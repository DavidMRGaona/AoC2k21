#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_vents(case):
    with open(f'{case}', 'r') as f:
        lines = [[[int(x) for x in p.split(',')] for p in line.split(' -> ')] for line in f.read().splitlines()]
    return lines


def calculate_vents(lines, filter_diag):
    # The diagram is somewhat an adjacent matrix
    lines_matrix = {}

    if filter_diag:
        lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lines))

    for p1, p2 in lines:

        # v is a transformation vector that indicates how the coordinates change when traveling along the segment.
        # * horizontal line left to right: v = [1, 0] / right to left: v = [-1, 0]
        # * vertical line top to bottom : v = [0, 1] / bottom to top: v = [0, -1]
        # * diagonal line is the resulting v of combining horizontal and vertical
        v = [0, 0]
        if p1[0] < p2[0]:
            v[0] += 1
        elif p1[0] > p2[0]:
            v[0] -= 1

        if p1[1] < p2[1]:
            v[1] += 1
        elif p1[1] > p2[1]:
            v[1] -= 1

        # x_s -> Starting point on x
        # x_e -> Ending point on x
        x_s = p1[0]
        x_e = p2[0]

        # y_s -> Starting point on x
        # y_e -> Ending point on x
        y_s = p1[1]
        y_e = p2[1]

        # Both x and y ending coords get a little modification in order to take the actual ending point into account.
        # For example, from (0,9) to (5,9) we want the while loop to end at (6,9)
        x_e += v[0]
        y_e += v[1]

        while x_s != x_e or y_s != y_e:
            # assign point to adj_matrix
            if x_s not in lines_matrix:
                lines_matrix[x_s] = {}
            if y_s not in lines_matrix[x_s]:
                lines_matrix[x_s][y_s] = 1
            else:
                lines_matrix[x_s][y_s] += 1

            # Update points
            if x_s != x_e:
                x_s += v[0]
            if y_s != y_e:
                y_s += v[1]

    return sum([y >= 2 for x in lines_matrix.values() for y in x.values()])


# Part 1.
print('Part 1...', end=' ')
lines = read_vents('input')
points = calculate_vents(lines, filter_diag=True)
print('Done!')
print(f'Found {points} points where at least two lines overlap')

# Part 2
print('Part 2...', end=' ')
lines = read_vents('input')
points = calculate_vents(lines, filter_diag=False)
print('Done!')
print(f'Found {points} points where at least two lines overlap')

from functools import cache

import numpy as np


@cache
def get_input():
    x_min, x_max = 128, 160
    y_mix, y_max = -142, -88
    return x_min, x_max, y_mix, y_max


def fire(velocity_x: int, velocity_y: int):
    x, y = 0, 0
    while True:
        x += velocity_x
        y += velocity_y
        yield x, y
        # drag
        if velocity_x > 0:
            velocity_x -= 1
        if velocity_x < 0:
            velocity_x += 1
        # gravity
        velocity_y -= 1


def get_highest_y(velocity_x: int, velocity_y: int):
    x_min, x_max, y_min, y_max = get_input()
    highest_y = 0
    for x, y in fire(velocity_x, velocity_y):
        highest_y = max(highest_y, y)
        if y < y_min:
            return None
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return highest_y


@cache
def grid_search():
    x_min, x_max, y_min, y_max = get_input()
    x_search = list(range(x_max + 1))
    y_search = list(range(y_min - 1, 750))
    grid = [[get_highest_y(x, y) for y in y_search] for x in x_search]
    grid = np.array(grid, dtype=np.float64)
    best_x_index, best_y_index = np.unravel_index(np.nanargmax(grid), grid.shape)
    return dict(
        max_height=int(np.nanmax(grid)),
        best_x=x_search[best_x_index],
        best_y=y_search[best_y_index],
        n_hits=np.count_nonzero(~np.isnan(grid)),
    )


print(
    "Max reachable height {max_height} via velocity x={best_x}, y={best_y}. Total velocities that hit {n_hits}".format(
        **grid_search()
    ))

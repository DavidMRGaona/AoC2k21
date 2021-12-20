from functools import cache
from pathlib import Path

import numpy as np


def read_input(pad_width=10):
    path = Path(__file__).parent.joinpath("input")
    pixel_map, image = Path(path).read_text().split("\n\n")
    image = [list(line) for line in image.splitlines()]
    image = np.array(image)
    image = np.pad(image, pad_width=pad_width, constant_values=".")
    return pixel_map, image


def get_replacement_pixel(image, pixel_map, i, j):
    return pixel_map[
        int(
            "".join(image[i - 1: i + 2, j - 1: j + 2].flatten())
                .replace(".", "0")
                .replace("#", "1"),
            base=2,
        )
    ]


def refine(image, pixel_map):
    output = np.full_like(image, fill_value=".")
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            output[i, j] = get_replacement_pixel(image, pixel_map, i, j)
    return output


@cache
def multi_refine(n_times=2):
    pixel_map, image = read_input(pad_width=n_times * 2 + 10)
    for iteration in range(n_times):
        image = refine(image, pixel_map)
        if iteration % 2 == 1:
            image = image[3:-3, 3:-3]
            image = np.pad(image, pad_width=3, constant_values=".")
    return (image == "#").sum()


print("part 1", multi_refine(n_times=2))

print("part 2", multi_refine(n_times=50))

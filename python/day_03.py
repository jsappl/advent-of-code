"""Day 3: Toboggan Trajectory"""

import numpy as np


def decode(line: str) -> list:
    """Generate binary list from string."""
    decoded = []
    for char in line:
        if char == ".":
            decoded.append(0)
        else:  # means char == "#"
            decoded.append(1)
    return decoded


def read_from(file_: str) -> "np.array":
    """Read slope data from file."""
    slope = []
    with open(file_, "r") as f:
        for line in f.readlines():
            slope.append(decode(line[:-1]))  # omit newline
    return np.array(slope, dtype=int)


def skiing_on(slope: "np.array", right: int, down: int) -> int:
    """Ski on given slope according to right/down and count encountered trees."""
    pos_x, pos_y = 0, 0
    n_trees = 0
    while pos_x < slope.shape[0]:
        # count tree at current position
        n_trees += slope[pos_x, pos_y]
        # ski to new position
        pos_x += down
        pos_y = (pos_y + right) % slope.shape[1]
    return n_trees


def main():
    file_ = "../assets/data/03.txt"
    slope = read_from(file_)

    # part one
    n_trees = skiing_on(slope, 3, 1)
    print(f"While skiing on the slope you encountered a total of {n_trees} trees.")

    # part two
    product_trees = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        product_trees *= skiing_on(slope, right, down)
    print(f"For different skiing patterns the product of encountered trees is {product_trees}.")


if __name__ == "__main__":
    main()

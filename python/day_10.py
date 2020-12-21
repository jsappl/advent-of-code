"""Day 10: Adapter Array"""

from typing import Tuple

import numpy as np


def read_data_from(file_: str) -> list:
    """Read port output from file."""
    with open(file_, "r") as f:
        return list(map(int, f.readlines()))


def distribution_of(joltages: list) -> Tuple[int, int]:
    """Get 1-jolt and 3-jolt differences distribution."""
    differences = list(np.diff(np.array(sorted([0] + joltages))))
    return differences.count(1), differences.count(3) + 1


def distinct_ways_of(group: list, current: int) -> list:
    """Recursive program for how adapters in group can be arranged."""
    if current == group[-1]:
        return [[current]]
    paths = []
    for tolerance in range(1, 4):
        if current + tolerance in group:
            for path in distinct_ways_of(group, current + tolerance):
                paths.append([current] + path)
    return paths


def count_ways_in(joltages: list) -> int:
    """Count total number of distinct adapter arrangements."""
    n_ways = 1
    joltages = [0] + sorted(joltages) + [max(joltages) + 3]  # add plug and device
    differences = list(np.diff(np.array(joltages)))
    group = []  # init
    for idx, diff in enumerate(differences):
        group.append(joltages[idx])
        if diff == 3:
            n_ways *= len(distinct_ways_of(group, group[0]))
            group = []  # reset
    return n_ways


def main():
    file_ = "../assets/data/10.txt"
    joltages = read_data_from(file_)

    # part one
    one_diff, three_diff = distribution_of(joltages)
    print(f"Product of one- and three-jolt differences is {one_diff*three_diff}.")

    # part two
    n_ways = count_ways_in(joltages)
    print(f"Distinct ways of arranging adapters is {n_ways}.")


if __name__ == "__main__":
    main()

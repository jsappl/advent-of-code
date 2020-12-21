"""Day 1: Report Repair"""

from typing import Tuple

import numpy as np


def read(file_: "str") -> "np.array":
    """Read data from file."""
    return np.genfromtxt(file_, dtype="int")


def find_two_entries(data: "np.array") -> Tuple["int", "int"]:
    """Check array for the two entries that sum to 2020."""
    for idx, j in enumerate(data[:-1]):
        for k in data[idx + 1:]:
            if j + k == 2020:
                return j, k


def find_three_entries(data: "np.array") -> Tuple["int", "int", "int"]:
    """Check array for the three entries that sum to 2020."""
    for idx0, p in enumerate(data[:-1]):
        for idx1, q in enumerate(data[idx0 + 1:]):
            for r in data[idx1 + 1:]:
                if p + q + r == 2020:
                    return p, q, r


def main():
    file_ = "./assets/data/01.txt"
    data = read(file_)

    # part one
    j, k = find_two_entries(data)
    print(f"Found integers {j} and {k}. Their sum is {j+k}, their product is {j*k}.")

    # part two
    p, q, r = find_three_entries(data)
    print(f"Found integers {p}, {q}, and {r}. Their sum is {p+q+r}, their product is {p*q*r}.")


if __name__ == "__main__":
    main()

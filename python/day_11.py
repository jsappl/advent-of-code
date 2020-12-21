"""Day 11: Seating System"""

from typing import Callable

import numpy as np


def read_data_from(file_: str) -> np.ndarray:
    """Get seat data from file."""
    seats = []
    file_io = open(file_, "r")
    for line in file_io:
        seats.append(list(line[:-1]))
    return np.array(seats)


def apply_rules_to(seats: np.ndarray) -> np.ndarray:
    """Apply the two seating rules to seats."""
    rows, cols = np.shape(seats)
    seats = np.pad(seats, 1, constant_values=".")
    new_seats = np.copy(seats)
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            adjacent = seats[row - 1:row + 2, col - 1:col + 2].flatten().tolist()
            if seats[row][col] == "L" and adjacent.count("#") == 0:
                new_seats[row][col] = "#"
            elif seats[row][col] == "#" and adjacent.count("#") >= 5:
                new_seats[row][col] = "L"
    return new_seats[1:-1, 1:-1]


def apply_new_rules_to(seats: np.ndarray) -> np.ndarray:
    """Apply the new seating rules to seats."""
    rows, cols = np.shape(seats)
    new_seats = np.copy(seats)
    for row in range(rows):
        for col in range(cols):
            occupied = 0
            for direction in np.array([[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]):
                scale = 0
                while True:
                    scale += 1
                    new_row, new_col = [row, col] + scale * direction
                    if new_row == -1 or new_row == rows or new_col == -1 or new_col == cols:
                        break
                    if seats[new_row, new_col] == "#":
                        occupied += 1
                        break
                    if seats[new_row, new_col] == "L":
                        break
            if seats[row][col] == "#" and occupied >= 5:
                new_seats[row][col] = "L"
            elif seats[row][col] == "L" and occupied == 0:
                new_seats[row][col] = "#"
    return new_seats


def converge(seats: np.ndarray, rules: Callable) -> np.ndarray:
    """Iterate seating rules until seats converge."""
    while True:
        new_seats = rules(seats)
        if np.array_equal(seats, new_seats):
            return new_seats
        seats = new_seats
        new_seats = np.zeros_like(seats)  # reset


def main():
    file_ = "../assets/data/11.txt"
    seats = read_data_from(file_)

    # part one
    final = converge(seats, apply_rules_to)
    print(f"After converging {final.flatten().tolist().count('#')} seats are occupied.")

    # part two
    final = converge(seats, apply_new_rules_to)
    print(f"After converging with new rules {final.flatten().tolist().count('#')} seats are occupied.")


if __name__ == "__main__":
    main()

"""Day 12: Rain Risk"""

from typing import Tuple

import numpy as np


def read_data_from(file_: str) -> list:
    """Get directions of travel from file."""
    file_io = open(file_, "r")
    instructions = []
    for line in file_io:
        instructions.append((line[0], int(line[1:])))
    return instructions


def move_ferry_with(instructions: list) -> Tuple[int, int]:
    """Navigate ferry according to navigation instructions."""
    direction = 0
    moves = {"N": 0, "S": 0, "E": 0, "W": 0}
    for action, value in instructions:
        if action == "F":
            moves[["E", "N", "W", "S"][direction % 360 // 90]] += value
            continue
        try:  # move in specific direction
            moves[action] += value
        except KeyError:  # turn the ferry
            direction += ((action == "L") - (action == "R")) * value  # turn
    return moves["N"] - moves["S"], moves["E"] - moves["W"]


def rot90(vector: np.ndarray, direction: str, k: int) -> np.ndarray:
    """Rotate vector in 2D plane."""
    if direction == "R":  # convert to "L"
        k = abs(360 - k * 90) // 90
        direction = "L"
    for _ in range(k):
        vector = np.multiply([-1, 1], np.flip(vector))
    return vector


def move_ferry_with_new(instructions: list) -> np.ndarray:
    """Navigate ferry according to new navigation instructions."""
    waypoint = np.array([10, 1])  # W/E and N/S directions
    position = np.zeros(2, int)
    for action, value in instructions:
        if action == "F":
            position += value * waypoint
            continue
        waypoint[0] += ((action == "E") - (action == "W")) * value
        waypoint[1] += ((action == "N") - (action == "S")) * value
        if action in ("L", "R"):
            waypoint = rot90(waypoint, action, value // 90)
    return position


def main():
    file_ = "../assets/data/12.txt"
    instructions = read_data_from(file_)

    # part one
    pos_x, pos_y = move_ferry_with(instructions)
    print(f"Manhattan distance of {abs(pos_x) + abs(pos_y)}.")

    # part two
    position = move_ferry_with_new(instructions)
    print(f"With new instructions Manhattan distance of {sum(abs(position))}.")


if __name__ == "__main__":
    main()

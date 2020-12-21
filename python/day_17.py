"""Day 17: Conway Cubes"""

import numpy as np


def read_data_from(file_: str) -> np.ndarray:
    """Read initial cube state from file."""
    actives = open(file_, "r").read().splitlines()
    actives = np.array([[[char == "#"] for char in line] for line in actives])
    return np.pad(actives, 6 + 1, "constant", constant_values=False)


def execute_cycle(actives: np.ndarray) -> np.ndarray:
    """Execute one cyle of energy source boot up."""
    next_actives = np.zeros_like(actives) * False
    it = np.nditer(actives[1:-1, 1:-1, 1:-1], flags=["multi_index"])
    for active in it:
        idx, idy, idz = it.multi_index
        idx += 1
        idy += 1
        idz += 1
        active_neighbors = np.sum(actives[idx - 1:idx + 2, idy - 1:idy + 2, idz - 1:idz + 2])
        if active and active_neighbors in [1 + 2, 1 + 3]:
            next_actives[idx, idy, idz] = True
        elif not active and active_neighbors == 3:
            next_actives[idx, idy, idz] = True
    return next_actives


def execute_4d_cycle(actives: np.ndarray) -> np.ndarray:
    """Execute one cyle of energy source boot up in 4D."""
    next_actives = np.zeros_like(actives) * False
    it = np.nditer(actives[1:-1, 1:-1, 1:-1, 1:-1], flags=["multi_index"])
    for active in it:
        idx, idy, idz, idw = it.multi_index
        idx += 1
        idy += 1
        idz += 1
        idw += 1
        active_neighbors = np.sum(actives[idx - 1:idx + 2, idy - 1:idy + 2, idz - 1:idz + 2, idw - 1:idw + 2])
        if active and active_neighbors in [1 + 2, 1 + 3]:
            next_actives[idx, idy, idz, idw] = True
        elif not active and active_neighbors == 3:
            next_actives[idx, idy, idz, idw] = True
    return next_actives


def main():
    # part one
    actives = read_data_from("../assets/data/17.txt")
    for _ in range(6):
        actives = execute_cycle(actives)
    print(f"Total of {np.sum(actives)} cubes are active.")

    # part one
    actives = read_data_from("../assets/data/17.txt")
    actives = np.pad(np.expand_dims(actives, -1), ((0, 0), (0, 0), (0, 0), (7, 7)), "constant", constant_values=False)
    for _ in range(6):
        actives = execute_4d_cycle(actives)
    print(f"Total of {np.sum(actives)} cubes are active in four dimensions.")


if __name__ == "__main__":
    main()

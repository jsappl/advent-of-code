"Day 24: Lobby Layout"

from collections import defaultdict


def read_data_from(file_: str) -> list:
    """Return which tiles to flip."""
    paths = []
    fio = open(file_, "r")
    for line in fio:
        paths.append(list(line.rstrip()))
    return paths


def flip_tiles_in(paths: list) -> set:
    """Return black tiles after flipping."""
    black = set()
    dir_ = {"e": (2, 0), "se": (1, -1), "sw": (-1, -1), "w": (-2, 0), "nw": (-1, 1), "ne": (1, 1)}
    for path in paths:
        pos_x, pos_y = 0, 0
        while path:
            next_ = path.pop(0)
            if next_ not in dir_.keys():
                next_ += path.pop(0)
            pos_x, pos_y = pos_x + dir_[next_][0], pos_y + dir_[next_][1]
        if (pos_x, pos_y) not in black:
            black.add((pos_x, pos_y))
        else:
            black.remove((pos_x, pos_y))
    return black


def art_exhibit(black: set) -> set:
    """Flip tiles for the art exhibition."""
    dir_ = {"e": (2, 0), "se": (1, -1), "sw": (-1, -1), "w": (-2, 0), "nw": (-1, 1), "ne": (1, 1)}
    for _ in range(100):
        flips = set()
        white = defaultdict(int)
        for pos in black:
            b_neighbors = 0
            for next_ in dir_.values():
                new = (pos[0] + next_[0], pos[1] + next_[1])
                if new in black:
                    b_neighbors += 1
                else:
                    white[new] += 1
            if not 1 <= b_neighbors <= 2:
                flips.add(pos)  # flip black to white
        black = black.difference(flips).union({pos for pos, count in white.items() if count == 2})
    return black


def main():
    paths = read_data_from("../assets/data/24.txt")

    # part one
    black = flip_tiles_in(paths)
    print(f"After flipping {len(black)} tiles are black.")

    # part two
    black = art_exhibit(black)
    print(f"For the art exhibition {len(black)} tiles are black.")


if __name__ == "__main__":
    main()

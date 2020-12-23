"Day 23: Crab Cups"

from typing import Tuple


def split(cups: list) -> Tuple[int, list, list]:
    """Split cups in crab game."""
    return cups[0], cups[1:4], cups[4:]


def place(pick: list, rest: list, dest: int) -> list:
    """Place picked up cups after destination."""
    idx = rest.index(dest)
    return rest[:idx + 1] + pick + rest[idx + 1:]


def play_crab(cups: list) -> list:
    """Play a game of crab cups."""
    for _ in range(100):
        curr, pick, rest = split(cups)
        dest = curr - 1
        while dest not in rest:
            if dest < min(rest):
                dest = max(rest)
                break
            dest -= 1
        cups = place(pick, rest, dest) + [curr]
    return cups


def play_proper_crab(cups: list) -> Tuple[int, int]:
    """Play the crab game with many more cups."""
    n_cups = 1000000
    # Init linked list next_ which maps cup to next cup.
    cups = cups + [max(cups) + 1]
    next_ = ["X"] + [cup + 2 for cup in range(n_cups - 1)] + [cups[0]]  # index starts with 1
    for idx, cup in enumerate(cups[:-1]):
        next_[cup] = cups[idx + 1]

    curr = cups[0]
    for _ in range(10000000):
        start = next_[curr]  # start of pick
        next_[curr] = next_[next_[next_[start]]]  # skip pick
        pick = start, next_[start], next_[next_[start]]

        dest = curr - 1 if curr > 1 else n_cups
        while dest in pick:
            dest -= 1 if dest > 1 else n_cups

        next_[next_[next_[start]]] = next_[dest]  # update next at end of pick
        next_[dest] = start  # insert pick after destination

        curr = next_[curr]  # go to next current
    return next_[1], next_[next_[1]]


def main():
    cups = list(map(int, "389547612"))

    # part one
    final = play_crab(cups)
    idx = final.index(1)
    print("Labels on cups are", "".join(map(str, final[idx + 1:] + final[:idx])), "after cup 1.")

    # part two
    final = play_proper_crab(cups)
    print(f"Product of cup labels next to cup 1 is {final[0]*final[1]}.")


if __name__ == "__main__":
    main()

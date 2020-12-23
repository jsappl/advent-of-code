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


def play_proper_crab(head: list) -> list:
    """Play the crab game with many more cups."""
    tail = [1000000]
    count = 10
    for _ in range(10000000):
        curr, pick, rest = split(head + tail)
        dest = curr - 1
        while dest not in rest:
            if dest < min(rest):
                dest = max(rest)
                count += 1
                break
            dest -= 1
        if dest in tail:
            add = list(range(count, count + 3))
            count += 3
        else:
            add = [count]
            count += 1
        full = place(pick, rest, dest)
        head = full[:full.index(1000000)] + add
        tail = full[full.index(1000000):] + [curr]
    return head + tail


def main():
    cups = [3, 8, 9, 5, 4, 7, 6, 1, 2]

    # part one
    final = play_crab(cups)
    idx = final.index(1)
    print("Labels on cups are", "".join(map(str, final[idx + 1:] + final[:idx])), "after cup 1.")

    # part two
    play_proper_crab(cups)


if __name__ == "__main__":
    main()

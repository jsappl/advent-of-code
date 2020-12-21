"""Day 13: Shuttle Search"""

from math import prod
from typing import Tuple


def read_data_from(file_: str) -> Tuple[int, list]:
    """Earliest departure time and bus ID."""
    lines = open(file_, "r").read().splitlines()
    return int(lines[0]), lines[1].split(",")


def earliest_bus_at(timestamp: int, bus_ids: list) -> Tuple[int, int]:
    """Find the earliest bus that goes to the airport."""
    difference = []
    for bus in bus_ids:
        difference.append(bus - timestamp % bus)
    return bus_ids[difference.index(min(difference))], min(difference)


def chinese_remainder(multiples: list, remainders: list) -> int:
    """The famous Chinese Remainder Theorem."""
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    int_prod = prod(multiples)
    return sum(b * (int_prod // n) * pow(int_prod // n, -1, n) for b, n in zip(remainders, multiples)) % int_prod


def main():
    file_ = "../assets/data/13.txt"
    timestamp, bus_ids = read_data_from(file_)

    # part one
    bus_id, min_difference = earliest_bus_at(timestamp, [int(b) for b in bus_ids if b != "x"])
    print(f"Earliest bus ID times number of minutes to wait is {bus_id*min_difference}.")

    # part two
    inputs = [(int(x), int(x) - p) for p, x in enumerate(bus_ids) if x != "x"]
    earliest = chinese_remainder([x[0] for x in inputs], [x[1] for x in inputs])
    print(f"Earliest time bus offsets match positions in list is {earliest}.")


if __name__ == "__main__":
    main()

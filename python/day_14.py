"""Day 14: Docking Data"""

import re
from itertools import product


def read_data_from(file_: str) -> list:
    """Read bitmasks and values from file."""
    return open(file_, "r").read().splitlines()


def apply_(mask: str, value: str) -> int:
    """Apply binmask to value."""
    bin_value = "{0:b}".format(int(value)).zfill(36)
    return int("".join([m if m != "X" else b for m, b in zip(mask, bin_value)]), 2)


def memory_address_decoder(mask: str, loc: str) -> list:
    """Bitmask modifies the bits of destination memory address."""
    bin_value = "{0:b}".format(int(loc)).zfill(36)
    locs = []
    indices = [i for i, letter in enumerate(mask) if letter == "X"]
    for floating in product(*[(0, 1)] * len(indices)):
        tmp = ""
        n_float = 0  # floating number index
        for idx, char in enumerate(mask):
            if char == "0":
                tmp += bin_value[idx]
            elif char == "1":
                tmp += char
            else:
                tmp += str(floating[n_float])
                n_float += 1
        locs.append(tmp)
    return list(map(lambda x: str(int(x, 2)), locs))


def execute_initialization(lines: list, part: str) -> list:
    """Execute the initialization program with binmasks."""
    memory = {}
    for line in lines:
        if "mask" in line:
            mask = line[-36:]
        else:
            loc, value = re.findall(r"(\d+)", line)
            if part == "one":
                memory[loc] = apply_(mask, value)
            else:  # part == "two"
                for new_loc in memory_address_decoder(mask, loc):
                    memory[new_loc] = int(value)
    return memory


def main():
    file_ = "../assets/data/14.txt"
    lines = read_data_from(file_)

    # part one
    memory = execute_initialization(lines, "one")
    print(f"Sum of all values left in memory is {sum(memory.values())}.")

    # part two
    memory = execute_initialization(lines, "two")
    print(f"Sum of all values left in memory with proper decoding is {sum(memory.values())}.")


if __name__ == "__main__":
    main()

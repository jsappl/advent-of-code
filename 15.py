"""Day 15: Rambunctious Recitation"""


def read_numbers_from(file_: str) -> list:
    """Read starting numbers from file."""
    return list(map(int, open(file_, "r").read().split(",")))


def memory_game(numbers: list, abort: int) -> int:
    """Play the North Pole memory game."""
    memory = {number: idx for idx, number in enumerate(numbers[:-1])}
    current = numbers[-1]
    turn = len(numbers) - 1
    while turn < abort - 1:
        if current in memory.keys():
            tmp = current
            current = turn - memory[current]
            memory[tmp] = turn
        else:
            memory[current] = turn
            current = 0
        turn += 1
    return current


def main():
    file_ = "./assets/data/15.txt"
    start = read_numbers_from(file_)

    # part one
    abort = 2020
    number = memory_game(start, abort)
    print(f"The {abort}th number spoken is {number}.")

    # part two
    abort = 30000000
    number = memory_game(start, abort)
    print(f"The {abort}th number spoken is {number}.")


if __name__ == "__main__":
    main()

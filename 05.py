"""Day 5: Binary Boarding"""

from typing import Tuple


def read_data_from(file_: str) -> list:
    """Read boarding pass data from file."""
    with open(file_, "r") as f:
        return f.read().splitlines()


def decode_seat_of(pass_: list, n_rows: int = 128, n_cols: int = 8) -> Tuple[int, int]:
    """Return row and column number from boarding pass information."""
    row_range = [1, n_rows]
    col_range = [1, n_cols]

    for char in pass_[:7]:  # decode row
        if char == "F":
            row_range[1] -= (row_range[1] - row_range[0] + 1) // 2
        elif char == "B":
            row_range[0] += (row_range[1] - row_range[0] + 1) // 2

    for char in pass_[7:]:  # decode column
        if char == "L":
            col_range[1] -= (col_range[1] - col_range[0] + 1) // 2
        elif char == "R":
            col_range[0] += (col_range[1] - col_range[0] + 1) // 2
    return row_range[0] - 1, col_range[0] - 1


def seat_status_from(passes: list, n_rows: int = 128, n_cols: int = 8) -> list:
    """Return binary matrix indicating occupied seats on the plane."""
    seats = n_rows * n_cols * [False]  # init with zeros
    for pass_ in passes:
        row, col = decode_seat_of(pass_)
        seats[row * 8 + col] = True
    return seats


def find_my_seat_from(seats: list) -> int:
    """Find my empty seat in the airplane."""
    for seat_id, taken in enumerate(seats):
        if not taken and seats[seat_id - 1] is True and seats[seat_id + 1] is True:
            return seat_id


def main():
    file_ = "./assets/data/05.txt"
    passes = read_data_from(file_)

    # part one
    seat_ids = []
    for pass_ in passes:
        row, col = decode_seat_of(pass_)
        seat_ids.append(row * 8 + col)
    print(f"The highest seat ID is {max(seat_ids)}.")

    # part two
    seats = seat_status_from(passes)
    my_seat = find_my_seat_from(seats)
    print(f"My empty seat is {my_seat}.")


if __name__ == "__main__":
    main()

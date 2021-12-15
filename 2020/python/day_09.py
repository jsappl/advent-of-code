"""Day 9: Encoding Error"""


def read_data_from(file_: str) -> list:
    """Read port output from file."""
    with open(file_, "r") as f:
        return list(map(int, f.readlines()))


def possible_sums_of(numbers: list) -> list:
    """Compute all possible sums of numbers excluding self."""
    possible_sums = []
    for idx, nr_0 in enumerate(numbers[:-1]):
        for nr_1 in numbers[idx + 1:]:
            possible_sums.append(nr_0 + nr_1)
    return possible_sums


def find_mismatch_in(output: list) -> int:
    """Return first number which is not a sum of previous ones."""
    for idx, number in enumerate(output[25:]):
        possible_sums = possible_sums_of(output[idx:idx + 25])
        if number not in possible_sums:
            return idx + 25, number


def find_contiguous_in(output: list, error_idx: int) -> list:
    """Find contiguous set of at least two numbers with the sum."""
    nr = 2
    while True:
        for idx in range(len(output[:error_idx]) - nr):
            if sum(output[idx:idx + nr]) == output[error_idx]:
                return output[idx:idx + nr]
        nr += 1


def main():
    file_ = "../assets/data/09.txt"
    output = read_data_from(file_)

    # part one
    idx, number = find_mismatch_in(output)
    print(f"The number {number} is not the sum of previous ones.")

    # part two
    contiguous = find_contiguous_in(output, idx)
    print(f"Encryption weakness is {min(contiguous)+max(contiguous)}.")


if __name__ == "__main__":
    main()

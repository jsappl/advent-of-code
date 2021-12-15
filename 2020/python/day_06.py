"""Day 6: Custom Customs"""


def read_from(file_: str) -> list:
    """Read answers from file."""
    answers_per_group = []
    answers = []  # init
    with open(file_, "r") as f:
        for line in f.readlines():
            if not line[:-1]:  # omit \n character
                answers_per_group.append(answers)
                answers = []  # reset
            else:
                answers.append(line[:-1])
    return answers_per_group


def count_yes_in(answers: list) -> int:
    """Count distinctive 'yes' answers in group."""
    return len(set("".join(answers)))


def count_all_yes_in(answers: list) -> int:
    """Count answers in group which everybody answered 'yes'."""
    return len(set.intersection(*[set(a) for a in answers]))


def main():
    # CAVE: Add bottom empty line otherwise read_from won't work.
    file_ = "../assets/data/06.txt"
    answers_per_group = read_from(file_)

    # part one
    n_yes = 0
    for answers in answers_per_group:
        n_yes += count_yes_in(answers)
    print(f"Total of {n_yes} 'yes' answers.")

    # part two
    n_all_yes = 0
    for answers in answers_per_group:
        n_all_yes += count_all_yes_in(answers)
    print(f"Total of {n_all_yes} all 'yes' answers.")


if __name__ == "__main__":
    main()

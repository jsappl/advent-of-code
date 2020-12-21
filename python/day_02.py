"""Day 2: Password Philosophy"""


def data_from(file_: "str") -> list:
    """Returns data from given file."""
    data = []
    with open(file_, "r") as f:
        for line in f.readlines():
            data.append(line.replace("-", " ").replace(":", "").split())
    return data


def count(char: "str", pw: "str") -> int:
    """Count character in password."""
    n_match = 0
    for x in pw:
        if char == x:
            n_match += 1
    return n_match


def check_valid(policy_and_pw: "list") -> bool:
    """Check whether password policy is met or not."""
    min_, max_, char, pw = policy_and_pw
    n_match = count(char, pw)
    if n_match < int(min_) or n_match > int(max_):
        return False
    else:
        return True


def check_valid_new(policy_and_pw: "list") -> bool:
    """Check whether new password policy is met or not."""
    pos0, pos1, char, pw = policy_and_pw
    if (pw[int(pos0) - 1] == char) + (pw[int(pos1) - 1] == char) == 1:
        return True
    else:
        return False


def main():
    file_ = "../assets/data/02.txt"
    data = data_from(file_)

    # part one
    n_valid = 0
    for policy_and_pw in data:
        if check_valid(policy_and_pw):
            n_valid += 1

    print(f"A total of {n_valid} passwords are valid according to their policies.")

    # part two
    n_valid = 0
    for policy_and_pw in data:
        if check_valid_new(policy_and_pw):
            n_valid += 1

    print(f"A total of {n_valid} passwords are valid according to the new policies.")


if __name__ == "__main__":
    main()

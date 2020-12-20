"Day 19: Monster Messages"

from typing import Tuple

import regex as re


def read_data_from(file_: str) -> Tuple[dict, list]:
    """Get rules and messages from file."""
    fio = open(file_, "r")
    rules = {}
    for line in fio:
        if line == "\n":
            break
        idx, rule = line.rstrip().split(": ")
        rules[int(idx)] = rule.replace('"', "")
    return rules, fio.read().splitlines()


def regex_from(rules: list, idx: int) -> str:
    """Return regex for zero rule."""
    possible = rules[idx]
    while re.search(r"(\d+)", possible):
        possible = re.sub(r"(\d+)", lambda x: "(" + rules[int(x.group(1))] + ")", possible)
    return possible.replace(" ", "")


def main():
    rules, messages = read_data_from("./assets/data/19.txt")

    # part one
    possible = regex_from(rules, 0)
    n_match = 0
    for message in messages:
        n_match += bool(re.fullmatch(possible, message))
    print(f"A total of {n_match} messages completely match rule 0.")

    # part two
    rules[8] = "42 +"
    rules[11] = "(?P<group> 42 (?&group)? 31)"
    possible = regex_from(rules, 0)
    n_match = 0
    for message in messages:
        n_match += bool(re.fullmatch(possible, message))
    print(f"With regex loops {n_match} messages completely match rule 0.")


if __name__ == "__main__":
    main()

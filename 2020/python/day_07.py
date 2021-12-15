"""Day 7: Handy Haversacks"""

import re


def convert(inner: list) -> dict:
    """Return inner bags as dictionary."""
    out = {}
    if inner == ["no other"]:
        return out
    else:
        for bag in inner:
            out[bag[2:]] = int(bag[:2])
    return out


def read_data_from(file_: str) -> dict:
    """Read luggage rules from file."""
    rules = {}
    with open(file_, "r") as f:
        for line in f.readlines():
            for word in [" bag.\n", " bags.\n"]:
                line = line.replace(word, "")
            line = re.split(" bags contain | bag, | bags, ", line)
            outer = line[0]
            inner = line[1:]
            rules[outer] = convert(inner)
    return rules


def shiny_gold_in(bag: str, rules: dict) -> bool:
    """Recursively check for shiny gold bags."""
    if "shiny gold" in rules[bag].keys():
        return True
    elif not rules[bag]:  # bag holds no others
        return False
    else:
        for inner in rules[bag]:
            if shiny_gold_in(inner, rules):
                return True
        return False  # no inner bag contains shiny gold


def count_inner_bags_of(outer: str, rules: dict) -> int:
    """Recursively count all bags inside the outer one."""
    n_inner = sum(rules[outer].values())  # how many inside
    for inner, count in rules[outer].items():  # count bags inside the insides
        n_inner += count * count_inner_bags_of(inner, rules)
    return n_inner


def main():
    file_ = "../assets/data/07.txt"
    rules = read_data_from(file_)

    # part one
    bags = []
    for bag in rules:
        if shiny_gold_in(bag, rules):
            bags.append(bag)
    print(f"A total of {len(bags)} bags contain at least one shiny gold one.")

    # part two
    outer = "shiny gold"
    n_inner = count_inner_bags_of(outer, rules)
    print(f"A {outer} bag has to contain {n_inner} bags.")


if __name__ == "__main__":
    main()

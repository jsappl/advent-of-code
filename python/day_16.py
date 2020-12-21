"""Day 16: Ticket Translation"""

import re
from typing import Tuple


def read_data_from(file_: str) -> Tuple[dict, list, list]:
    """Read rules for, numbers on your, and numbers on nearby tickets."""
    file_str = open(file_, "r").read().splitlines()
    rules = {}
    for rule in file_str[:20]:
        key, b0, e0, b1, e1 = re.split(": |-| or ", rule)
        rules[key] = [int(b0), int(e0), int(b1), int(e1)]
    yours = list(map(int, file_str[22].split(",")))
    nearby = []
    for ticket in file_str[25:]:
        nearby.append(list(map(int, ticket.split(","))))
    return rules, yours, nearby


def in_field_of(rules: list, value: int) -> bool:
    """Check if value in any range of rules."""
    for b0, e0, b1, e1 in rules.values():
        if b0 <= value <= e0 or b1 <= value <= e1:
            return True
    return False


def find_completely_invalid(tickets: list, rules: dict) -> Tuple[int, list]:
    """Find invalid tickets with values not valid for any field."""
    error_rate = 0
    valid = []
    for ticket in tickets:
        skip = False
        for value in ticket:
            if not in_field_of(rules, value):
                error_rate += value
                skip = True
        if not skip:
            valid.append(ticket)
    return error_rate, valid


def determine_fields_from(valid: list, rules) -> list:
    """Determine in which order the fields appear on the tickets."""
    order = {}
    positions = list(range(len(valid[0])))
    while rules:
        for pos in positions:
            possible = []
            for rule, (b0, e0, b1, e1) in rules.items():
                all_in_range = True
                for ticket in valid:
                    if not (b0 <= ticket[pos] <= e0 or b1 <= ticket[pos] <= e1):
                        all_in_range = False
                if all_in_range:
                    possible.append(rule)
            if len(possible) == 1:
                order[pos] = possible[0]
                rules.pop(possible[0])
                positions.remove(pos)
                break
    return order


def main():
    rules, yours, nearby = read_data_from("../assets/data/16.txt")

    # part one
    error_rate, valid = find_completely_invalid(nearby, rules)
    print(f"Ticket scanning error rate is {error_rate}.")

    # part two
    order = determine_fields_from(valid, rules)
    product = 1
    for pos, rule in order.items():
        if "departure" in rule:
            product *= yours[pos]
    print(f"Multiplying those six values together gives {product}.")


if __name__ == "__main__":
    main()

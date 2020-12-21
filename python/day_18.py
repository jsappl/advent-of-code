"""Day 18: Operation Order"""

import re
from typing import Callable


def read_data_from(file_: str) -> list:
    """Read math homework from file."""
    return open(file_, "r").read().splitlines()


def new_rules(expression: str) -> str:
    """Evaluate expression with new rules."""
    n_mult = expression.count("*")
    expression = expression.replace("*", ")*")
    expression = n_mult * "(" + expression
    return str(eval(expression))


def add_before_mult(expression: str) -> str:
    """Evaluate addition before multiplication."""
    while re.search(r"(\d+\s\+\s\d+)", expression):
        expression = re.sub(r"(\d+\s\+\s\d+)", lambda x: str(eval(x.group(1))), expression)
    return str(eval(expression))


def evaluate(homework: list, rule: Callable) -> list:
    """Evaluate math homework with different rules."""
    results = []
    for exercise in homework:
        while re.search(r"(\([^()]*\))", exercise):
            exercise = re.sub(r"(\([^()]*\))", lambda x: rule(x.group(1)), exercise)
        results.append(int(rule(exercise)))
    return results


def main():
    homework = read_data_from("./assets/data/18.txt")

    # part one
    results = evaluate(homework, new_rules)
    print(f"Sum of the resulting values is {sum(results)}.")

    # part two
    results = evaluate(homework, add_before_mult)
    print(f"Sum with addition before multiplication is {sum(results)}.")


if __name__ == "__main__":
    main()

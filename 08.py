"""Day 8: Handheld Halting"""


def read_data_from(file_: str) -> list:
    """Read boot code from file."""
    with open(file_, "r") as f:
        return f.read().splitlines()


def execute(code: list) -> int:
    """Return accumulator value. Stop if infinite loop."""
    accumulator = 0
    executed = []
    current = 0
    while current not in executed and current != len(code):
        operation, argument = code[current].split()
        executed.append(current)
        if operation == "acc":
            accumulator += int(argument)
            current += 1
        elif operation == "jmp":
            current += int(argument)
        else:  # No OPeration
            current += 1
    return accumulator, current


def fix(code: list) -> int:
    """Fix faulty boot code in brute force fashion."""
    for idx, line in enumerate(code):
        operation, _ = line.split()
        if operation == "jmp":
            code[idx] = line.replace("jmp", "nop")
        else:
            code[idx] = line.replace("nop", "jmp")
        accumulator, current = execute(code)
        if current == len(code):
            return accumulator
        else:
            code[idx] = line


def main():
    file_ = "./assets/data/08.txt"
    code = read_data_from(file_)

    # part one
    accumulator, current = execute(code)
    print(f"Accumulator of {accumulator} right before infinite loop.")

    # part two
    accumulator = fix(code)
    print(f"Accumulator of {accumulator} in fixed boot loader.")


if __name__ == "__main__":
    main()

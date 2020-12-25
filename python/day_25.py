"Day 25: Combo Breaker"


def find_loop_size_of(key: int) -> int:
    """Determine loop size from public key."""
    value = 1
    subject = 7
    loop = 0
    while value != key:
        value *= subject
        value = value % 20201227
        loop += 1
    return loop


def calculate_encryption(first_key: int, second_key: int) -> int:
    """Calculate encryption key with loop size and other device's public key."""
    value = 1
    for _ in range(find_loop_size_of(second_key)):
        value *= first_key
        value = value % 20201227
    return value


def main():
    key_card = 11562782
    key_door = 18108497

    # part one
    encryption = calculate_encryption(key_card, key_door)
    print(f"The encryption key is {encryption}.")


if __name__ == "__main__":
    main()

"""Day 22: Crab Combat"""

from copy import deepcopy


def read_data_from(file_: str) -> list:
    """Retrieve starting decks for players."""
    fio = open(file_, "r")
    decks = []
    deck = []
    for line in fio:
        if line.rstrip().isdigit():
            deck.append(int(line))
        elif line == "\n":
            decks.append(deck)
            deck = []
    return decks


def combat(decks: list) -> list:
    """Play a game of Combat with given starting decks."""
    while decks[0] and decks[1]:
        cards = [decks[0].pop(0), decks[1].pop(0)]
        if cards[0] > cards[1]:
            decks[0] += cards
        else:
            decks[1] += cards[::-1]
    return decks[0 if decks[0] else 1]  # return winner


def compute_score_of(winner: list) -> int:
    """Compute score of winning deck."""
    return sum((idx + 1) * card for idx, card in enumerate(winner[::-1]))


def recursive_combat(decks: list) -> int:
    """Play a game of Recursive Combat with given starting decks."""
    previous = []
    while decks[0] and decks[1]:
        if decks in previous:
            return 0  # player 1 wins
        previous.append(deepcopy(decks))
        cards = [decks[0].pop(0), decks[1].pop(0)]  # deal cards
        if len(decks[0]) >= cards[0] and len(decks[1]) >= cards[1]:
            winner = recursive_combat([decks[0][:cards[0]], decks[1][:cards[1]]])
        else:
            winner = 0 if cards[0] > cards[1] else 1
        decks[winner] += cards if winner == 0 else cards[::-1]
    return 0 if decks[0] else 1


def main():
    decks = read_data_from("../assets/data/22.txt")

    # part one
    winner = combat(deepcopy(decks))
    print(f"After playing the winner has a score of {compute_score_of(winner)}.")

    # part two
    winner = recursive_combat(decks)
    winner = decks[winner]
    print(f"After playing Recursive Combat the winner has a score of {compute_score_of(winner)}.")


if __name__ == "__main__":
    main()

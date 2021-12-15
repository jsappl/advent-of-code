"""Day 21: Allergen Assessment"""

from typing import Tuple


def read_data_from(file_: str) -> dict:
    """Get ingredients and allergens from file."""
    foods = {}
    fio = open(file_, "r")
    for idx, food in enumerate(fio):
        foods[idx] = {
            "ingredients": food.split(" (")[0].split(" "),
            "allergens": food[:-2].split("(contains ")[1].split(", ")
        }
    return foods


def analyze(foods: dict) -> Tuple[list, list]:
    """Return all ingredients and allergens in foods."""
    ingredients = []
    allergens = []
    for food in foods.values():
        ingredients += food["ingredients"]
        allergens += food["allergens"]
    return list(set(ingredients)), list(set(allergens))


def intersect(foods: dict, allergen: str) -> list:
    """Intersect ingredients for fixed allergen in foods."""
    ingredients_per_allergen = [set(food["ingredients"]) for food in foods.values() if allergen in food["allergens"]]
    return set.intersection(*ingredients_per_allergen)


def save_ingredients_from(foods: dict) -> list:
    """Return ingredients which cannot contain allergens."""
    save = []
    ingredients, allergens = analyze(foods)
    for ingredient in ingredients:
        is_save = True
        for allergen in allergens:
            if ingredient in intersect(foods, allergen):
                is_save = False
        if is_save:
            save.append(ingredient)
    return save


def count(save: list, foods: dict) -> int:
    """Count occurrence of save ingredients in foods."""
    n_save = 0
    for food in foods.values():
        n_save += len(set(save).intersection(set(food["ingredients"])))
    return n_save


def find_connection(save: list, foods: dict) -> list:
    """Figure out which ingredient contains which allergen."""
    ingredients, allergens = analyze(foods)
    dangerous = {}
    while len(dangerous) < len(allergens):
        for allergen in allergens:
            possible = list(intersect(foods, allergen).difference(dangerous.keys()))
            if len(possible) == 1:
                dangerous[possible[0]] = allergen
    return sorted(dangerous, key=dangerous.get)


def main():
    foods = read_data_from("../assets/data/21.txt")

    # part one
    save = save_ingredients_from(foods)
    n_save = count(save, foods)
    print(f"In all foods save ingredients are used {n_save} times.")

    # part two
    dangerous = find_connection(save, foods)
    print(f"The canonical dangerous ingredient list is {dangerous}.")


if __name__ == "__main__":
    main()

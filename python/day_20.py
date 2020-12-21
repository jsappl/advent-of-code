"Day 20: Jurassic Jigsaw"

import numpy as np


def read_data_from(file_: str) -> dict:
    """Load image tiles from file."""
    tiles = {}
    tile = []
    for line in open(file_, "r").read().splitlines():
        if "Tile" in line:
            idx = int(line[5:-1])
        elif line == "":
            tiles[idx] = np.array(tile)
            tile = []
        else:
            tile.append(list(line))
    return tiles


def rotate_and_flip(tile: np.ndarray) -> list:
    """Get all rotated and flipped versions of single tile."""
    return [np.rot90(tile, k=times) for times in range(4)] + [np.rot90(np.fliplr(tile), k=times) for times in range(4)]


def find_first_corner(tiles: dict) -> int:
    """Return upper-left corner tile."""
    for corner_idx, tile in tiles.items():
        found_corner = True
        for idx, neighbor in tiles.items():
            if idx != corner_idx:
                for altered in rotate_and_flip(neighbor):
                    if np.all(tile[0, :] == altered[-1, :]) or np.all(tile[:, 0] == altered[:, -1]):
                        found_corner = False
        if found_corner:
            return corner_idx
    raise Exception("Should have returned earlier.")


def find_row(tiles: dict, left: int = None) -> list:
    """Align tiles in row based on leftmost tile."""
    indices = [left]
    tile = tiles[left]
    while len(indices) < 12:
        for idx, neighbor in tiles.items():
            if idx not in indices:
                for altered in rotate_and_flip(neighbor):
                    if np.all(tile[:, -1] == altered[:, 0]):
                        indices.append(idx)
                        tiles[idx] = altered
                        tile = altered
                        break
    return indices


def find_next_left(tiles: dict, old: list) -> int:
    """Return next leftmost tile below old one."""
    tile = tiles[old[-1][0]]
    for idx, neighbor in tiles.items():
        if idx not in [x for y in old for x in y]:
            for altered in rotate_and_flip(neighbor):
                if np.all(tile[-1, :] == altered[0, :]):
                    tiles[idx] = altered
                    return idx
    raise Exception("Should have returned earlier.")


def reconstruct(tiles: dict) -> list:
    """Reconstruct image from tiles with matching edges."""
    for row in range(0, 12):
        if row == 0:
            left = find_first_corner(tiles)
            order = [find_row(tiles, left)]
        else:
            left = find_next_left(tiles, order)  # update leftmost in new row
            order.append(find_row(tiles, left))
    return order


def image_from(tiles: dict, order: list) -> np.ndarray:
    """Get image from order of tile indices."""
    image = np.empty((12 * 8, 12 * 8), int)
    for row in range(12):
        for col in range(12):
            image[row * 8:row * 8 + 8, col * 8:col * 8 + 8] = tiles[order[row][col]][1:-1, 1:-1] == "#"
    return image


def find(monster: np.ndarray, image: np.ndarray) -> int:
    """Detect sea monsters and determine roughness of the sea."""
    n_row, n_col = image.shape
    for altered in rotate_and_flip(image):
        n_monsters = 0
        for row in range(n_row - 2):
            for col in range(n_col - 19):
                subimage = altered[row:row + 3, col:col + 20]
                if np.sum(np.multiply(subimage, monster)) >= np.sum(monster):
                    n_monsters += 1
                    altered[row:row + 3, col:col + 20] -= monster
        if n_monsters > 0:
            return np.sum(altered == 1)
    raise Exception("Should have returned earlier.")


def main():
    tiles = read_data_from("../assets/data/20.txt")

    # part one
    order = reconstruct(tiles)
    print(f"Product of corners is {order[0][0]*order[0][-1]*order[-1][0]*order[-1][-1]}.")

    # part two
    monster = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        ])
    image = image_from(tiles, order)
    roughness = find(monster, image)
    print(f"Roughness of the sea is {roughness}.")


if __name__ == "__main__":
    main()

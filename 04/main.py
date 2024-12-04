"""Day 4: Ceres Search."""

import argparse


def main():
    """Parse word search and look for XMAS."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    rows = []
    with open(args.filename, mode="r", encoding="utf-8") as f:
        for line in f:
            rows.append(line)

    word = "XMAS"
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    total = 0
    for j, r in enumerate(rows):
        for i, c in enumerate(r):
            if c == "X":
                total += check_word(rows, word, directions, (i, j))

    print(total)


def check_word(
    puzzle: list[str],
    word: str,
    directions: list[tuple[int, int]],
    start: tuple[int, int],
) -> int:
    """Look for `word` along all legal `directions`."""
    total = 0
    for d in directions:
        if check_direction(puzzle, word, d, start):
            total += 1
    return total


def check_direction(
    puzzle: list[str],
    word: str,
    direction: tuple[int, int],
    start: tuple[int, int],
):
    """Look for `word` along `direction`."""
    for i, c in enumerate(word[1:]):
        row = start[1] + direction[1] * (i + 1)
        col = start[0] + direction[0] * (i + 1)
        if row < 0 or col < 0:
            return False
        try:
            letter = puzzle[row][col]
        except IndexError:
            return False
        if not letter == c:
            return False
    return True


if __name__ == "__main__":
    main()

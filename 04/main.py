"""Day 4: Ceres Search."""

import argparse


def main():
    """Parse word search and look for X-MAS."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    rows = []
    with open(args.filename, mode="r", encoding="utf-8") as f:
        for line in f:
            rows.append(line)

    total = 0
    for j, r in enumerate(rows):
        for i, c in enumerate(r):
            if c == "A":
                total += check(rows, (i, j))

    print(total)


def check(
    puzzle: list[str],
    start: tuple[int, int],
) -> int:
    """Search for two MAS's along diagonals."""
    word = "MAS"
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    total = 0
    for d in directions:
        if check_direction(puzzle, word, d, (start[0] - d[0], start[1] - d[1])):
            total += 1
    return 1 if total == 2 else 0


def check_direction(
    puzzle: list[str],
    word: str,
    direction: tuple[int, int],
    start: tuple[int, int],
):
    """Look for `word` along `direction`."""
    if start[0] < 0 or start[1] < 0:
        return False
    for i, c in enumerate(word):
        row = start[1] + direction[1] * (i)
        col = start[0] + direction[0] * (i)
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

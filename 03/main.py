"""Day 3: Mull It Over."""

import argparse

from parse.tokenize import tokenize_line


def main():
    """Parse an execute a program."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    total = 0
    with open(args.filename, mode="r", encoding="utf-8") as f:
        for line in f:
            tokens = tokenize_line(line)
            total += exec_line(tokens)
    print(total)


def exec_line(tokens: list[any]) -> int:
    """Execute a line of the program."""
    total = 0
    for i, t in enumerate(tokens):
        if t == "MUL(":
            total += exec_mul(tokens[i:]) or 0
    return total


def exec_mul(arr: list[any]) -> int | None:
    """
    Execute a potential mul statement.

    Return `None` if the mul is malformed.
    """
    if (
        isinstance(arr[1], int)
        and arr[2] == ","
        and isinstance(arr[3], int)
        and arr[4] == ")"
    ):
        return arr[1] * arr[3]
    return None


if __name__ == "__main__":
    main()

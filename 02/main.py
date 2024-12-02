"""Day 2: Red-Nosed Reports."""

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename, mode="r", encoding="utf-8") as f:
        num_safe = parse(f)

    print(num_safe)


def parse(f):
    total = 0
    for line in f:
        if is_safe([int(s, 10) for s in str.split(line)]):
            total += 1
    return total


def is_safe(report: list[int]) -> bool:
    """
    Check if a report is safe.

    A report is safe only if:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    adj_pairs = lambda: zip(report[:-1], report[1:])
    incr = all(i < j for i, j in adj_pairs())
    decr = all(i > j for i, j in adj_pairs())
    grad = all(1 <= abs(i - j) and abs(i - j) <= 3 for i, j in adj_pairs())
    return (incr or decr) and grad


if __name__ == "__main__":
    main()

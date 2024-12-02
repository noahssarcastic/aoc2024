"""Day 2: Red-Nosed Reports."""

import argparse


def main():
    """Determine the number of safe reports."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename, mode="r", encoding="utf-8") as f:
        num_safe = parse(f)

    print(num_safe)


def parse(f):
    """Parse a list of reports and find the number that are safe."""
    total = 0
    for line in f:
        report = [int(s, 10) for s in str.split(line)]
        if is_safe(report) or is_safe_ish(report):
            total += 1
    return total


def adj_pairs(arr: list[any]) -> zip:
    """Create a zip iterator of the adjacent pairs of a list."""
    return zip(arr[:-1], arr[1:])


def is_safe_ish(report: list[int]) -> bool:
    """Check if a report is safe after removing one element."""
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True
    return False


def is_safe(report: list[int]) -> bool:
    """
    Check if a report is safe.

    A report is safe only if:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    return (strict_incr(report) or strict_decr(report)) and gradual(report)


def strict_incr(arr: list[int]) -> bool:
    """Check if a list of ints is strictly increasing."""
    return all(i < j for i, j in adj_pairs(arr))


def strict_decr(arr: list[int]) -> bool:
    """Check if a list of ints is strictly decreasing."""
    return all(i > j for i, j in adj_pairs(arr))


def gradual(arr: list[int]) -> bool:
    """
    Check if a list of ints is changing gradually.

    A gradual change is a difference of between 1 and 3 inclusive.
    """
    return all(1 <= abs(i - j) and abs(i - j) <= 3 for i, j in adj_pairs(arr))


if __name__ == "__main__":
    main()

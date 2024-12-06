"""Day 5: Print Queue."""

import argparse
import math


def main():
    """Check page ordering."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    page_order = []
    updates = []
    with open(args.filename, mode="r", encoding="utf-8") as f:
        for line in f:
            if line.isspace():
                break
            page_order.append([int(x, 10) for x in line.strip().split("|")])
        for line in f:
            updates.append([int(x, 10) for x in line.strip().split(",")])

    total = 0
    for u in updates:
        if in_order(u, page_order):
            total += u[math.floor(len(u) / 2)]
    print(total)


def in_order(arr, lookup) -> bool:
    """Check if page numbers are in order."""
    for i, a in enumerate(arr):
        for _j, b in enumerate(arr[i + 1 :]):
            if not is_before(a, b, lookup):
                return False
                # print(f"moving {a}@{i} to after {b}@{j}")
                # arr.insert(j, arr.pop(i))
    return True


def is_before(a: int, b: int, lookup) -> bool:
    """Check if page `a` is before page `b`."""
    # print(f"checking if {a} is before {b}")
    for rule in lookup:
        if rule[0] == b and rule[1] == a:
            return False
    return True


if __name__ == "__main__":
    main()

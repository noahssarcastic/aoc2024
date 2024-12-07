"""Day 5: Print Queue."""

import argparse
import math
import time


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
        reordered, fixes = reorder(u, page_order)
        if fixes == 0:
            continue
        middle_idx = math.floor(len(u) / 2)
        total += reordered[middle_idx]
    print(total)


def reorder(arr: list[int], lookup) -> list[int]:
    """Fix ordering of `arr` and track the number of fixes."""
    fixes = 0
    while True:
        temp = fix_unsorted(arr, lookup)
        if temp is None:
            break
        arr = temp
        fixes += 1
    return arr, fixes


def fix_unsorted(arr: list[int], lookup) -> list[int] | None:
    """Look for an ordering mistake and correct it."""
    for i, a in enumerate(arr):
        # Look for an ordering mistake starting from the back
        for j in range(len(arr) - 1, i, -1):
            b = arr[j]
            if is_before(a, b, lookup):
                continue
            # Move a to after b at index j
            arr.insert(j, arr.pop(i))
            return arr
    return None


def is_before(a: int, b: int, lookup) -> bool:
    """Check if page `a` is before page `b`."""
    for rule in lookup:
        if rule[0] == b and rule[1] == a:
            return False
    return True


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Execution time is :", (end - start) * 10**3, "ms")

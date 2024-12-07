"""Day 5: Print Queue."""

import argparse
from collections import defaultdict
import math
import time


def main():
    """Check page ordering."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    page_order = defaultdict(list)
    updates = []
    with open(args.filename, mode="r", encoding="utf-8") as f:
        for line in f:
            if line.isspace():
                break
            first, second = line.strip().split("|")
            page_order[first].append(second)
        for line in f:
            updates.append(line.strip().split(","))

    total = 0
    for u in updates:
        reordered, fixes = reorder(u, page_order)
        if fixes == 0:
            continue
        middle_idx = math.floor(len(u) / 2)
        total += int(reordered[middle_idx], 10)
    print(total)


def reorder(arr, lookup) -> tuple[list, int]:
    """Fix ordering of `arr` and track the number of fixes."""
    fixes = 0
    while True:
        temp = fix_unsorted(arr, lookup)
        if temp is None:
            break
        arr = temp
        fixes += 1
    return arr, fixes


def fix_unsorted(arr, lookup) -> list | None:
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


def is_before(a, b, lookup) -> bool:
    """Check if page `a` is before page `b`."""
    return b in lookup.get(a, [])


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Execution time is :", (end - start) * 10**3, "ms")

"""Day 1: Historian Hysteria."""

import argparse


def main():
    """
    Determine the similarity score of two lists.

    Calculate a total similarity score by adding up each number in the left list
    after multiplying it by the number of times that number appears in the right list.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename, mode="r", encoding="utf-8") as f:
        first, second = parse(f)

    second.sort()
    total_similarity = 0
    for i in first:
        total_similarity += i * similarity(i, second)

    print(total_similarity)


def parse(f):
    """Parse a file and return two integer lists."""
    first = []
    second = []
    for line in f:
        split = line.split()
        first.append(int(split[0], 10))
        second.append(int(split[1], 10))
    return first, second


def similarity(num, arr):
    """
    Find the number of times `num` appears in `arr`.

    Expects `arr` to be sorted.
    """
    count = 0
    for i in arr:
        if num > i:
            continue
        if num == i:
            count += 1
            continue
        if num < i:
            break
    return count


if __name__ == "__main__":
    main()

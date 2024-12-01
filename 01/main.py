import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename, mode="r", encoding="utf-8") as f:
        parse(f)


def parse(f):
    first = []
    second = []
    for line in f:
        split = line.split()
        first.append(split[0])
        second.append(split[1])
    first.sort()
    second.sort()
    total = 0
    for i, k in enumerate(first):
        total += abs(int(k, 10) - int(second[i], 10))
    print(total)


if __name__ == "__main__":
    main()

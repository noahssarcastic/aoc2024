"""Day 6: Guard Gallivant."""

import argparse
from enum import Enum
import time


class Direction(Enum):
    """Represent the four cardinal direction."""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def next(self):
        """Get the next direction in clockwise order."""
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + 1
        if index >= len(members):
            index = 0
        return members[index]


class OutOfBoundsError(Exception):
    """An out-of-bounds move was detected."""

    def __init__(self, *args):
        super().__init__(*args)


class Map:
    """Represent map data."""

    def __init__(self, inp: list[str]):
        self.data = inp
        self.rows = len(self.data)
        self.cols = len(self.data[0])
        for y, row in enumerate(self.data):
            x = row.find("^")
            if x >= 0:
                self.dir = Direction.UP
                self.pos = (x, y)
                break
            x = row.find(">")
            if x >= 0:
                self.dir = Direction.RIGHT
                self.pos = (x, y)
                break
            x = row.find("v")
            if x >= 0:
                self.dir = Direction.DOWN
                self.pos = (x, y)
                break
            x = row.find("<")
            if x >= 0:
                self.dir = Direction.LEFT
                self.pos = (x, y)
                break

        self.visited = [self.pos]

        # Replace current guard position with empty space.
        temp = list(self.data[self.pos[1]])
        temp[self.pos[0]] = "."
        self.data[self.pos[1]] = "".join(temp)

    def is_obstacle(self, coord: tuple[int, int]) -> bool:
        """Is the cell at `coord` an obstruction?"""
        return self.data[coord[1]][coord[0]] == "#"

    def next_pos(self) -> tuple[int, int]:
        """Get the guard's next position."""
        match self.dir:
            case Direction.UP:
                return (self.pos[0], self.pos[1] - 1)
            case Direction.RIGHT:
                return (self.pos[0] + 1, self.pos[1])
            case Direction.DOWN:
                return (self.pos[0], self.pos[1] + 1)
            case Direction.LEFT:
                return (self.pos[0] - 1, self.pos[1])

    def move(self) -> None:
        """
        Move the guard following the puzzle rules.

        If there is something directly in front of you, turn right 90 degrees.
        Otherwise, take a step forward.
        """
        next_pos = self.next_pos()
        if self.out_of_bounds(next_pos):
            raise OutOfBoundsError()
        if self.is_obstacle(next_pos):
            self.dir = self.dir.next()
            return
        if next_pos not in self.visited:
            self.visited.append(next_pos)
        self.pos = next_pos

    def out_of_bounds(self, coord: tuple[int, int]) -> bool:
        """Is the cell at `coord` out-of-bounds?"""
        return (
            coord[0] < 0
            or self.cols <= coord[0]
            or coord[1] < 0
            or self.rows <= coord[1]
        )


def main():
    """Calculate the guard's path."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    puzzle = []
    with open(args.filename, mode="r", encoding="utf-8") as f:
        for line in f:
            puzzle.append(line)

    map_data = Map(puzzle)
    while True:
        try:
            map_data.move()
        except OutOfBoundsError:
            break
    print(len(map_data.visited))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Execution time is:", (end - start) * 10**3, "ms")

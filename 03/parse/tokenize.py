"""Utilities for tokenizing the puzzle input."""

import collections
from itertools import islice


def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is None, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        collections.deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)


def tokenize_line(line: str):
    """Convert a string to an array of tokens."""
    tokens = []
    cursor = iter(range(len(line)))
    for i in cursor:
        s = line[i:]
        val = None
        x = 0
        if is_mul_start(s):
            val, x = parse_mul_start(s)
        if is_int(s):
            val, x = parse_int(s)
        if is_directive_end(s):
            val, x = parse_directive_end(s)
        if is_comma(s):
            val, x = parse_comma(s)
        tokens.append(val)
        consume(cursor, x)
    return tokens


def is_mul_start(s: str) -> bool:
    """Check if next token is a mul directive."""
    return s[:4] == "mul("


def parse_mul_start(_s: str) -> tuple[str, int]:
    """
    Generate a mul token from a string.

    Also return the number of extra characters consumed.
    """
    return "MUL(", 3


def is_directive_end(s: str) -> bool:
    """Check if next token is directive end."""
    return s[0] == ")"


def parse_directive_end(_s: str) -> tuple[str, int]:
    """
    Generate a directive end token from a string.

    Also return the number of extra characters consumed.
    """
    return ")", 0


def is_int(s: str) -> bool:
    """Check if next token is an integer."""
    try:
        int(s[0])
    except ValueError:
        return False
    return True


def parse_int(s: str) -> tuple[int, int]:
    """
    Generate an int token from a string.

    Also return the number of extra characters consumed.
    """
    full_int = ""
    for i in s:
        try:
            int(i)
        except ValueError:
            break
        full_int += i
    return int(full_int, 10), len(full_int) - 1


def is_comma(s: str) -> bool:
    """Check if next token is a comma."""
    return s[0] == ","


def parse_comma(_s: str) -> tuple[str, int]:
    """
    Generate a comma token from a string.

    Also return the number of extra characters consumed."""
    return ",", 0

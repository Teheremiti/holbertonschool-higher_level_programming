#!/usr/bin/python3
"""Module with a function that prints out a square of '#'s"""

def print_square(size):
    """Print out a square with the char '#' of the size determined by the
    'size' argument."""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

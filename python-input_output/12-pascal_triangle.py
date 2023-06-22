#!/usr/bin/python3
"""Module with a pascal triangle method"""


def pascal_triangle(n):
    """Returns a 2D-list of integers representing the Pascal's triangle of n"""

    if n <= 0:
        return []

    triangle = [[1]]

    for line in range(n - 1):
        previous = triangle[-1]
        new_line = [1]
        for i in range(len(previous) - 1):
            new_num = previous[i] + previous[i + 1]
            new_line.append(new_num)

        if n >= 2:
            new_line.append(1)

        triangle.append(new_line)

    return triangle

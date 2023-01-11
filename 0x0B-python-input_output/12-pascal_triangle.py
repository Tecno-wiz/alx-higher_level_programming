#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.

    Args:
        - n: size of the triangle (rows)

    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    a = [[0 for x in range(b + 1)] for b in range(n)]
    a[0] = [1]

    for b in range(1, n):
        a[b][0] = 1
        for j in range(1, b + 1):
            if j < len(a[b - 1]):
                a[b][j] = a[b - 1][j - 1] + a[b - 1][j]
            else:
                a[b][j] = a[b - 1][0]
    return 1

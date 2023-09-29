#!/usr/bin/python3
"""
Interview prep questions
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the pascal triangly of n
    """
    result = []
    if n <= 0:
        return result

    for row in range(n):
        new_list = []
        for col in range(row + 1):
            if col == 0 or col == row:
                new_list.append(1)
            else:
                value = result[-1][col - 1] + result[-1][col]
                new_list.append(value)
        result.append(new_list)
    return result

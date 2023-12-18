#!/usr/bin/python3
"""Island perimeter problem solution"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    count = 0
    if len(grid) == 0 or len(grid[0]) == 0:
        return count

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                if i == 0 or grid[i - 1][j] == 0:
                    count += 1
                if j == 0 or grid[i][j - 1] == 0:
                    count += 1
                if i == (len(grid) - 1) or grid[i + 1][j] == 0:
                    count += 1
                if j == (len(grid[0]) - 1) or grid[i][j + 1] == 0:
                    count += 1
    return count

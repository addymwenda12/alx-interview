#!/usr/bin/python3
"""
This module calculates
the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Parameters:
    grid (list): A 2D list of integers where
    0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.

    """
    rows = len(grid)
    cols = len(grid[0])

    result = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r-1][c] == 0:
                    result += 1
                if r == rows-1 or grid[r+1][c] == 0:
                    result += 1
                if c == 0 or grid[r][c-1] == 0:
                    result += 1
                if c == cols-1 or grid[r][c+1] == 0:
                    result += 1

    return result

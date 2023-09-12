#!/usr/bin/python3
"""
Task 12
"""


def pascal_triangle(n):
    """
    Return the pascal triangle
    """
    if n <= 0:
        return []
    triangle = []
    for row in range(n):
        current_row = []

        for j in range(row + 1):
            if j == 0 or j == row:
                current_row.append(1)
            else:
                previous_row = triangle[row - 1]
                current_value = previous_row[j - 1] + previous_row[j]
                current_row.append(current_value)

        triangle.append(current_row)
    return triangle

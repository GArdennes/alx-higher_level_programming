#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix: the matrix to be divided
        div: the divisor

    Returns:
        A new matrix with all elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If each row of the matrix is not of the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
        if len(row) != len(matrix[0]):
            raise TypeError("each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix

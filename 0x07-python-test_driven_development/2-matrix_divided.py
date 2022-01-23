#!/usr/bin/python3
"""
This module contains matrix functions
"""


def matrix_divided(matrix, div):
    """Divide all element of a matrix by div"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    sizes = []
    if matrix is None or type(matrix) != list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for element in matrix:
        if type(element) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        sizes.append(len(element))
        for elements in element:
            if type(elements) not in [int, float]:
                raise TypeError(
                    "matrix \
must be a matrix (list of lists) of integers/floats")

    for element in sizes:
        size = sizes[0]
        if size != element:
            raise TypeError("Each row of the matrix must have the same size")
    return list(
        map(lambda arr: list((
            map(lambda val: round(val/div, 2), arr))), matrix))

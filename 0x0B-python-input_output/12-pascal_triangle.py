#!/usr/bin/python3
"""module for pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of list of integers representing the
    Pascal's triangle of n"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    list = [[1], [1, 1]]
    for i in range(2, n):
        sublist = [1]
        result = 0
        for k in range(1, i + 1):
            if k >= len(list[i - 1]):
                sublist.append(1)
            else:
                result = list[i - 1][k - 1] + list[i - 1][k]
                sublist.append(result)
        list.append(sublist)
    return list

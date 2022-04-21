#!/usr/bin/python3
"""Module find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    length = len(list_of_integers)
    if length == 0:
        return None
    else:
        list_of_integers.sort()
        return list_of_integers[-1]

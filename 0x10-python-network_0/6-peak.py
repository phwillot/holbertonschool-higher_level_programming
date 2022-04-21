#!/usr/bin/python3
"""Module find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    length = len(list_of_integers)
    if length == 0:
        return None
    elif length == 1:
        return list_of_integers[0]
    else:
        for i in range(0, length - 1):
            peak = list_of_integers[i]
            if i == 0 and length <= 1:
                if peak > list_of_integers[i + 1]:
                    return peak
            else:
                if peak >= list_of_integers[i - 1] and\
                        peak >= list_of_integers[i + 1]:
                    return peak

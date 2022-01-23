#!/bin/usr/python3
"""
This module contains the add function
"""


def add_integer(a, b=98):
    """Returns the sum of a + b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    else:
        try:
            a = int(a)
        except Exception:
            raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        try:
            b = int(b)
        except Exception:
            raise TypeError("b must be an integer")
    return a + b

#!/usr/bin/python3
"""Square module.

This modules contains a class who defines a square class

"""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes the data"""

        """size: Size of the square"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return square of the area"""
        return self.__size ** 2

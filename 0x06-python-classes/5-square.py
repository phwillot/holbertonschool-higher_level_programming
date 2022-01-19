#!/usr/bin/python3
"""Square module.
This module contains a class who defines a square class.
"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes the data
        size: size of the square"""
        self.size = size

    @property
    def size(self):
        """getter to access the size value
        Return: (int) size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Update the size value
        Value: int (size of the square)
        Raises: TypeError if type is not int
                ValueError if size < 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square root of the square"""
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with "#" """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()

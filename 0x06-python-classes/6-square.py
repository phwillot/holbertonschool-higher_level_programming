#!/usr/bin/python3
"""Square module.
This module contains a class who defines a square class.
"""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data
        size: size of the square
        position: Deplace the square starting point"""
        self.size = size
        self.position = position

    @property
    def position(self):
        """getter to access the position value
        Return: (tuple) position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Update the position value
        Value: tuple (position)
        Raises: TypeError if the value are not positive
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
             raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        return self.size ** 2

    def my_print(self):
        """ Prints the square with "#" and check position too"""
        if self.__size == 0:
            print()
        for k in range(self.position[1]):
            print()
        else:
            for i in range(self.__size):
                for p in range(self.position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()

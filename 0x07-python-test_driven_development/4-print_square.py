#!/usr/bin/python3
"""
This module contain Square functions
"""


def print_square(size):
    """ print_square - Prints a square with # based on size argument
    @size: Size of the square (int)
    Return: None
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        return

    for _ in range(size):
        for _ in range(size):
            print("{:s}".format("#"), end="")
        print()

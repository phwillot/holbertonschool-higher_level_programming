#!/usr/bin/python3
"""Module that contains the class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a Square"""
    def __init__(self, size):
        """Initialize the instance"""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

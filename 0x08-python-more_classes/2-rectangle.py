#!/usr/bin/python3
"""This module contains Rectangle class."""


class Rectangle:
    """Defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize the instance
        @width: width of rectangle
        @height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        """area: Return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter: Return the perimeter of the rectangle"""
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

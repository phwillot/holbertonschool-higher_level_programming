#!/usr/bin/python3
"""This module contain class Rectangle that inherits from BaseGeometry Class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines a Rectangle"""
    def __init__(self, width, height):
        """Initialize the class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string with dimensions of the rectangle"""
        return "[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height)

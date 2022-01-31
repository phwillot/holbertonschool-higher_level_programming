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

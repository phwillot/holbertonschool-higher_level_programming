#!/usr/bin/python3
"""This module contain a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

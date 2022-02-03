#!/usr/bin/python3
"""This module contains the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the instance of the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return the area of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with
        the character #"""
        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """return a sentence with the
        dimensions and axes of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

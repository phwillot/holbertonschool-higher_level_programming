#!/usr/bin/python3
"""This module contains Rectangle class."""


class Rectangle:
    """Defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the instance
        @width: width of rectangle
        @height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a string of the rectangle with # characters"""
        representation = []

        if self.__width == 0 or self.__height == 0:
            return ""
        for _ in range(self.__height):
            for _ in range(self.__width):
                representation.append(str(self.print_symbol))
            representation.append("\n")
        return "".join(representation[:-1])

    def __repr__(self):
        """Returns a string representation of the rectangle
        to be able to recreate a new instance using eval()"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Do these instruction when a instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal - Checks if area of rect_1 and rect_2
        are equal
        @rect_1: Instance of Rectangle
        @rect_2: Instance of Rectangle
        Return: rect_1 if both areas are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        elif rect_1.area() == rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """square - Return a new Rectangle instance with the same
        size and height
        @size: size of the new Rectangle
        Return: New Rectangle instance of the class Rectangle"""
        return cls(size, size)

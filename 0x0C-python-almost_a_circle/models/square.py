#!/usr/bin/python3
"""This module will define the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init the instance of the class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the dimensions of the Square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter size value"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args) > 0:
            array = ["id", "size", "x", "y"]
            i = 0
            for arg in args:
                setattr(self, array[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "x": self.x, "size": self.width,
                "y": self.y}

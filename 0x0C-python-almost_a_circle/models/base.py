#!/usr/bin/python3
"""This module contains the class Base"""


class Base:
    """This class define the base of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init the instance of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

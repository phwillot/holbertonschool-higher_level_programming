#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """This class defines a Student
    Public instance attributes:
    first_name, last_name, age"""
    def __init__(self, first_name, last_name, age):
        """init the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation"""
        dict = {}
        if type(attrs) == list:
            for elt in attrs:
                if type(elt) == str:
                    if self.__dict__.get(elt):
                        dict[elt] = self.__dict__[elt]
                else:
                    return self.__dict__
            return dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value

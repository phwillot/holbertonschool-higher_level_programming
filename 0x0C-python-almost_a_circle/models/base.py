#!/usr/bin/python3
"""This module contains the class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to a file"""
        list = []
        for obj in list_objs:
            list.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list))

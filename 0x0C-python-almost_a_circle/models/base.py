#!/usr/bin/python3
"""This module contains the class Base"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to a file"""
        list = []
        for obj in list_objs:
            list.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        new = cls(2, 3)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        instance_list = []
        if not os.path.isfile(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as f:
            list = cls.from_json_string(f.read())
        for elt in list:
            instance_list.append(cls.create(**elt))
        return instance_list

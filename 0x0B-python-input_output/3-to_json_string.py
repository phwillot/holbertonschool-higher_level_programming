#!/usr/bin/python3
"""module with function to_json_string"""
import json


def to_json_string(my_obj):
    """Return the json representation of an object"""
    return json.dumps(my_obj)

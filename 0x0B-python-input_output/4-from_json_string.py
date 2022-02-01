#!/usr/bin/python3
"""module for function from_json_string"""
import json


def from_json_string(my_str):
    """Return object from a json string"""
    return json.loads(my_str)

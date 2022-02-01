#!/usr/bin/python3
"""module for function class_to_json"""


def class_to_json(obj):
    """Return dictionary description with simple data structure"""
    return obj.__dict__

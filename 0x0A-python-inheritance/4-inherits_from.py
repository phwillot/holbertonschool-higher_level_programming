#!/usr/bin/python3
"""Module for function inherits_from"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from the class"""
    return not issubclass(a_class, type(obj))

#!/usr/bin/python3
"""module function is_same_class"""


def is_same_class(obj, a_class):
    """is_same_class - Return True if object is an instance of the class
    @obj: object
    @a_class: class
    Return: True or False"""
    return type(obj) == a_class

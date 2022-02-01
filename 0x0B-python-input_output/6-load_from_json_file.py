#!/usr/bin/python3
"""module for function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file"
    """
    with open(filename, 'r') as F:
        return json.load(F)  # JSON ->>>> Object format

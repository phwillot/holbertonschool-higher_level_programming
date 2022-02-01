#!/usr/bin/python3
"""module for function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using Json representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)  # Object ->>>> JSON saved in to file

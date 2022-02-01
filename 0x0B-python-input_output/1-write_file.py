#!/usr/bin/python3
"""Module function write_file"""


def write_file(filename="", text=""):
    """Write into a file"""
    with open(filename, encoding="utf-8", mode="w") as myFile:
        return myFile.write(text)

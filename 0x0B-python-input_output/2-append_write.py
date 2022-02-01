#!/usr/bin/python3
"""Module with function append_write"""


def append_write(filename="", text=""):
    """Appends text to a file"""
    with open(filename, encoding="utf-8", mode="a") as FileName:
        return FileName.write(text)

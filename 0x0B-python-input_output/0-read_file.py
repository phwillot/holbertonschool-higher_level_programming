#!/usr/bin/python3
"""function that read text file and prints to stdout"""


def read_file(filename=""):
    """Reads a file"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")

#!/usr/bin/python3
"""Module Class MyList"""


class MyList(list):
    """Define a class MyList"""
    def print_sorted(self):
        """print the list in sorted ascending order"""
        print(sorted(self))

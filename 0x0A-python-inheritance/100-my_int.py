#!/usr/bin/python3
"""module for class myint"""


class MyInt(int):
    """Class MyInt"""

    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return not self.__eq__(other)

#!/usr/bin/python3
"""Unittest for max integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class to test the function max_integer
    """
    def test_max_value(self):
        """
        Simple tests with a normal list
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 3, 3]), 3)
        self.assertEqual(max_integer([3, 4, 3]), 4)
        self.assertEqual(max_integer([5, 3, 3]), 5)
        self.assertEqual(max_integer([-3, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-3, -5, -8]), -3)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([1]), 1)
        list = [3, -5, -float('inf')]
        self.assertEqual(max_integer(list), 3)
        list = [5000, -5200, float('inf')]
        self.assertEqual(max_integer(list), float('inf'))

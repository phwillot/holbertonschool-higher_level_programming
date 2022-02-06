#!/usr/bin/python3
"""Unittest for square.py module"""
from io import StringIO
from unittest import TestCase, mock
import unittest

from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class basicTesting(TestCase):
    """Tests cases for inheritance of methods Square->Rectangle"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str_method(self):
        result = "[Square] (1) 0/0 - 2"
        self.assertEqual(Square(2).__str__(), result)

    def test_str_method_x(self):
        result = "[Square] (1) 2/0 - 2"
        self.assertEqual(Square(2, 2).__str__(), result)

    def test_str_method_y(self):
        result = "[Square] (1) 2/2 - 2"
        self.assertEqual(Square(2, 2, 2).__str__(), result)

    def test_area_method(self):
        self.assertEqual(Square(2).area(), 4)

    def test_display_method(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            Square(2).display()
            self.assertEqual(output.getvalue(), "##\n##\n")

    def test_display_method_x(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            Square(2, 2).display()
            self.assertEqual(output.getvalue(), "  ##\n  ##\n")

    def test_display_method_y(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            Square(2, 2, 2).display()
            self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")

    def test_empty(self):
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


if __name__ == "__main__":
    unittest.main()

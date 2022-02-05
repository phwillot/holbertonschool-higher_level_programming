#!/usr/bin/python3
"""Unittest for rectangle.py module"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class testAttributeAndRaises(unittest.TestCase):
    """Tests Case for attribute of the Rectangle"""
    def setUp(self):
        Base._Base__nb_objects = 0

    # Attribute testing
    def test_width(self):
        self.assertEqual(Rectangle(3, 5).width, 3)

    def test_height(self):
        self.assertEqual(Rectangle(3, 5).height, 5)

    def test_x(self):
        self.assertEqual(Rectangle(3, 5, 1).x, 1)

    def test_y(self):
        self.assertEqual(Rectangle(3, 5, 1, 2).y, 2)

    def test_id_empty(self):
        self.assertEqual(Rectangle(3, 5).id, 1)

    def test_id_none(self):
        self.assertEqual(Rectangle(3, 5, 0, 0, None).id, 1)

    def test_id_positive(self):
        self.assertEqual(Rectangle(3, 5, 0, 0, 5).id, 5)

    def test_zero_id(self):
        self.assertEqual(Rectangle(3, 5, 1, 1, 0).id, 0)

    # Raise testing
    def test_rectangle_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_oneArg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_tooManyArguments(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_type_width(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 3)
        with self.assertRaises(TypeError):
            Rectangle(None, 23)
        with self.assertRaises(TypeError):
            Rectangle(["salut"], 3)

    def test_type_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "10")
        with self.assertRaises(TypeError):
            Rectangle(1, None)
        with self.assertRaises(TypeError):
            Rectangle(1, ["salut"])

    def test_type_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "10")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, None)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, ["salut"])

    def test_type_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "10")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, None)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, ["salut"])

    def test_value_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)

    def test_value_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)

    def test_value_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

    def test_value_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)


class testMethodArea(unittest.TestCase):
    """Tests for the area method of Rectangle class"""
    def test_calc_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(1, 1).area(), 1)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)


if __name__ == "__main__":
    unittest.main()

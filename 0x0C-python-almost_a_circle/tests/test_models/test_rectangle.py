#!/usr/bin/python3
"""Unittest for rectangle.py module"""
from io import StringIO
from unittest import TestCase, mock
import unittest

from models.rectangle import Rectangle
from models.base import Base


class testAttributeAndRaises(TestCase):
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


class testMethodArea(TestCase):
    """Tests for the area method of Rectangle class"""
    def test_calc_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(1, 1).area(), 1)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 5).area(10)


class testMethodDisplay(TestCase):
    """Tests for the display method of Rectangle class"""
    def test_width_and_height_only(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            Rectangle(2, 4).display()
            self.assertEqual(output.getvalue(), "##\n##\n##\n##\n")

    def test_with_x(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            Rectangle(2, 2, 1).display()
            self.assertEqual(output.getvalue(), " ##\n ##\n")

    def test_with_y(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            Rectangle(1, 2, 0, 1).display()
            self.assertEqual(output.getvalue(), "\n#\n#\n")

    def test_with_x_and_y(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            Rectangle(3, 3, 1, 2).display()
            self.assertEqual(output.getvalue(), "\n\n ###\n ###\n ###\n")

    def test_display_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2).display(5)


class testMethodStr(TestCase):
    """Tests for the __str__ method of Rectangle class"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_basic_print(self):
        result = "[Rectangle] (1) 0/0 - 2/4"
        with mock.patch("sys.stdout", new=StringIO()) as output:
            print(Rectangle(2, 4), end="")
            self.assertEqual(output.getvalue(), result)

    def test_with_str(self):
        result = "[Rectangle] (12) 1/0 - 3/6"
        self.assertEqual(Rectangle(3, 6, 1, 0, 12).__str__(), result)

    def test_with_strOfInstance(self):
        result = "[Rectangle] (50) 21/14 - 5/5"
        self.assertEqual(str(Rectangle(5, 5, 21, 14, 50)), result)

    def test_str_with_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3).__str__(23)


if __name__ == "__main__":
    unittest.main()

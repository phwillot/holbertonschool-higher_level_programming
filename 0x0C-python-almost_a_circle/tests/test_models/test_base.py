#!/usr/bin/python3
"""Unittest for base.py module"""
import unittest
from models.base import Base


class testBaseId(unittest.TestCase):
    """Tests cases for Base ID"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_empty_id(self):
        self.assertEqual(Base().id, 1)

    def test_none_id(self):
        self.assertEqual(Base(None).id, 1)

    def test_positive_id(self):
        self.assertEqual(Base(48).id, 48)

    def test_negative_id(self):
        self.assertEqual(Base(-5).id, -5)

    def test_zero_id(self):
        self.assertEqual(Base(0).id, 0)

    def test_mixed_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 4)

    def test_raise(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()

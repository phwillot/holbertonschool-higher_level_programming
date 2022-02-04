#!/usr/bin/python3
"""This module will contain unittest for the class Base"""
import unittest

from models.base import Base
from models.rectangle import Rectangle


class test_Base_class(unittest.TestCase):
    """Basic tests for Base class"""

    def test_id(self):
        self.assertEqual(Base(42).id, 42)

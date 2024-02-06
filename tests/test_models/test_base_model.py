#!/usr/bin/env python3
"""
================
Test base module
================
"""

import unittest
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """
    Test the base class
    """

    def setUp(self):
        """
        Executes once before each test case
        """
        b = BaseModel()

    def tearDown(self):
        """
        Cleans up after  each test case
        """
        pass

    def test_id_is_not_none(self):
        """
        Tests if id is not None
        """
        self.assertEqual(b, None)
    
    def test_id_is_unique(self):
        """
        Tests if id is unique
        """

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
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.mynumber = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("json of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    def setUp(self):
        """
        Executes once before each test case
        """
        pass

    def tearDown(self):
        """
        Cleans up after  each test case
        """
        pass

    def test_id_is_not_none(self):
        """
        Tests if id is not None
        """
        pass

if __name__ == "__main__":
    unittest.main()

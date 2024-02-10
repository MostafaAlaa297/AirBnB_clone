#!/usr/bin/env python3
"""
==================
FileStorage module
==================
"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    Serialize instances to JSON and JSON to instaneces
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __object the obj with the key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to json file_path
        """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open (FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(obj_dict, json_file)

    def reload (self):
        """
        Deserialize JSON to __objects
        """
        try:
            with open (FileStorage.__file_path, "r", encoding="utf-8") as json_file:
                obj_dict = json.load(json_file)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    cls = globals()[class_name]
                    obj_instance = cls(**obj_data)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

storage = FileStorage()
storage.reload()

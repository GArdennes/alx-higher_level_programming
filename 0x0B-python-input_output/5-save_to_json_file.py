#!/usr/bin/python3
"""
Task 5
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation
    Args:
        my_obj: The object to serialize
        filename: The name of the file to write to
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))

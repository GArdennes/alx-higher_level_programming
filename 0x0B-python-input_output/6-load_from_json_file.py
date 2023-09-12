#!/usr/bin/python3
"""
Task 6
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    Args:
        filename: the name of the file to read from
    Returns:
        the object represented by the JSON file
    """
    with open(filename, "r") as f:
        return json.loads(f.read())

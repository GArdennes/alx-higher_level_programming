#!/usr/bin/python3
"""
Task 4
"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON
    Args:
        my_str: The JSON stringto deserialize
    Returns:
        The object represented by the JSON string
    """
    return json.loads(my_str)

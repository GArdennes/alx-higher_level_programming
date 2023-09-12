#!/usr/bin/python3
"""
Task 8
"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure
    Args:
        obj: the object to serialize
    Returns:
        The dictionary description of the object
    """
    return obj.__dict___

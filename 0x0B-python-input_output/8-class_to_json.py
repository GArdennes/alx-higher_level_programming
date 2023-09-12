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
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, (str, int, bool)):
        return obj

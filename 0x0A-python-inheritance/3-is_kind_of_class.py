#!/usr/bin/python3
"""
Task 3
"""


def is_kind_of_class(obj, a_class):
    """Checks for inheritance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

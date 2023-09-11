#!/usr/bin/python3
"""
Task 4
"""


def inherits_from(obj, a_class):
    """Checks if object is directly or indirectly inheriting"""
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False

#!/usr/bin/python3
"""
Task 2
"""


def is_same_class(obj, a_class):
    """Checks instances"""
    if type(obj) is a_class:
        return True
    else:
        return False

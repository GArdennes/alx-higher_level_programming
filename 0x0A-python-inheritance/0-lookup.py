#!/usr/bin/python3
"""
Task 0 
"""

def lookup(obj):
    """ 
    Lookup function
    Args:
        obj: object
    """
    methods = []
    attributes = []

    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)

        if callable(attr):
            methods.append(attr_name)
        else:
            attributes.append(attr_name)
    return methods, attributes

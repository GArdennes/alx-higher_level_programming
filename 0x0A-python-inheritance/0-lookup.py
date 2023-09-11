#!/usr/bin/python3

def lookup(obj):
    """ Lookup function """
    methods = []
    attributes = []

    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)

        if callable(attr):
            methods.append(attr_name)
        else:
            attributes.append(attr_name)
    return methods, attributes

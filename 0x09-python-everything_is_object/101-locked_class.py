#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """Prevents user from dynamically creating new instance"""

    __slots__ = ["first_name"]

    def __init__(self):
        """class method"""

        self.first_name = "first_name"

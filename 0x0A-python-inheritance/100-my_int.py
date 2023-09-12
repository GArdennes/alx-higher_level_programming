#!/usr/bin/python3
"""
Task 100
"""


class MyInt(int):
    """MyInt class"""
    def __init__(self, value):
        """init method"""
        self.num = value

    def __eq__(self, other):
        """eq method"""
        return self.num != other

    def __ne__(self, other):
        """ne method"""
        return self.num == other

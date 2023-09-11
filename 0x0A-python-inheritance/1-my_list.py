#!/usr/bin/python3
"""
Task 1
"""


class MyList(list):
    """
    Subclass of list
    Args:
        list: class list
    """
    def print_sorted(self):
        """Class method"""
        sorted_list = sorted(self)
        print(sorted_list)

#!/usr/bin/python3
"""
Task 0
"""


def read_file(filename=""):
    """
    Reads the contents of a text file and prints it to stdout
    Args:
        filename: the name of the file to read
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text, end="")

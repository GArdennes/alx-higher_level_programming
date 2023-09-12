#!/usr/bin/python3
"""
Task 2
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8)

    Args:
        filename: the name of the file to append to
        text: the text to append to the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)

#!/usr/bin/python3
"""
Task 1
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8)
    Args:
        filename: the name of the file to write to
        text: the text to write to the file
    Returns:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)

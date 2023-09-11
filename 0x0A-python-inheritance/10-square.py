#!/usr/bin/python3
"""
Task 10
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass of BaseGeometry"""
    def __init__(self, size):
        """init method for subclass"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method"""
        return self.__size * self.__size

    def __str__(self):
        """string method"""
        return "[{}] {}/{}".format(
                "Rectangle", self.__size, self.__size)

#!/usr/bin/python3
"""
Task 8
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass constructor"""
    def __init__(self, width, height):
        """Define init method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Define area method"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """Define string method"""
        return "[{}] {}/{}".format(
                type(self).__name__, self.__width, self.__height)

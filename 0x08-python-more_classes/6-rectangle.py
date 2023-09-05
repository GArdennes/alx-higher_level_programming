#!/usr/bin/python3
"""Create a Rectangle class"""


class Rectangle:
    """A class to represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle."""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get theheight of the rectanble"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area fo teh rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimereter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string represntation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        result = ""
        for i in range(self.height):
            result += "#" * self.width + "\n"
        return result[:-1]

    def __repr__(self):
        """Return a prepresntation fo the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Decrement the number of instances"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

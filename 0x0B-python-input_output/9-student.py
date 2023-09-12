#!/usr/bin/python3
"""
Task 9
"""


class Student:
    """A class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student
        Args:
            first_name: the student's first name
            last_name: the student's last name
            age: the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the student
        """
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }

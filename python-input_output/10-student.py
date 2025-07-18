#!/usr/bin/python3
"""Student class with filtered JSON serialization"""


class Student:
    """Defines a student by first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of Student instance.
        If attrs is a list of strings, returns only those attributes.
        Otherwise, returns all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered[attr] = getattr(self, attr)
            return filtered
        else:
            return self.__dict__

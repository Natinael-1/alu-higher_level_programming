#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""

class Square:
    """This class represents a square with a private size attribute.

    The size of a square is crucial for computations like area,
    so it is kept private to control its value and type.
    """
    def __init__(self, size):
        """Initialize the square with the given size.

        Args:
            size: The size of the square.
        """
        self.__size = size

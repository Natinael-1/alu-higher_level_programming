#!/usr/bin/python3
"""This module defines a Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square shape that inherits Rectangle with equal sides."""

    def __init__(self, size):
        """Initialize Square with validated size.

        Args:
            size: The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"

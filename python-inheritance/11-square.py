#!/usr/bin/python3
"""module defines Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square that uses Rectangle's validation and area."""

    def __init__(self, size):
        """Initialize Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the Square description: [Square] <size>/<size>."""
        return f"[Square] {self.__size}/{self.__size}"

#!/usr/bin/python3


"""This module defines a Square class.

The Square class includes size validation and area computation.
"""


class Square:
    """This class represents a square with a private size attribute.

    The size of a square is crucial for computations like area,
    so it is kept private to control its value and type.
    """

    def __init__(self, size=0):
        """Initialize the square with the given size.

        Args:
            size: The size of the square, must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

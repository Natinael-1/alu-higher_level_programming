#!/usr/bin/python3


"""This module defines a Square class with size and position validation,
area computation, and printing the square with # characters.
"""


class Square:
    """This class represents a square with private size and position attributes.

    The size controls the dimensions, and the position controls
    the offset when printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with the given size and position.

        Args:
            size: The size of the square, must be an integer >= 0.
            position: A tuple of 2 positive integers for printing offset.

        Raises:
            TypeError: If size is not an integer or position is invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters with position offset.

        If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

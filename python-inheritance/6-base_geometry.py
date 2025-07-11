#!/usr/bin/python3
"""module defines BaseGeometry class with an unimplemented area."""


class BaseGeometry:
    """A base class for geometry operations."""

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

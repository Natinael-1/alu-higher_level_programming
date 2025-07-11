#!/usr/bin/python3
"""module defines function that checks for strict inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class (not direct instance)."""
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""module defines function that checks object inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance or inherits from a_class, else False."""
    return isinstance(obj, a_class)

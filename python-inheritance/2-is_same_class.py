#!/usr/bin/python3
"""module defines function that checks exact object type."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False."""
    return type(obj) is a_class

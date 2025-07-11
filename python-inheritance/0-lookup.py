#!/usr/bin/python3
""" module provides function that returns a list of attributes and methods."""


def lookup(obj):
    """Return list of attributes and methods of an object."""
    return dir(obj)

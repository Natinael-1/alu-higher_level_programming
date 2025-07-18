#!/usr/bin/python3
"""Function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Return the dictionary representation of a class instance.
    Args:
        obj: Instance of a class.
    Returns:
        dict: Attributes of the instance.
    """
    return obj.__dict__

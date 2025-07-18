#!/usr/bin/python3
"""Module that returns a Python object from a JSON string."""


def from_json_string(my_str):
    """Returns a Python data structure from a JSON string."""
    import json
    return json.loads(my_str)

#!/usr/bin/python3
"""Module that defines a function to append a string to a text file (UTF8)."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.
    Returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

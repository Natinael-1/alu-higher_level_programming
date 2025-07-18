#!/usr/bin/python3
"""Module that defines a function to read a UTF-8 text file
and print its contents.
"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

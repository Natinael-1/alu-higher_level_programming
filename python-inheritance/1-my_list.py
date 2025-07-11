#!/usr/bin/python3
"""module defines MyList, subclass of list with a print_sorted method."""


class MyList(list):
    """A subclass of list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order (without changing it)."""
        print(sorted(self))

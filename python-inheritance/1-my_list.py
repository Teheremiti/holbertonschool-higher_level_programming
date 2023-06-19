#!/usr/bin/python3
"""Module with a derived class"""


class MyList(list):
    """Derived class from 'list'"""

    def print_sorted(self):
        """Prints the the list, but sorted in ascending order.
        Assumes all elements will be of type int."""

        new = sorted(self[:])
        print(new)

#!/usr/bin/python3
"""Module with a function to list attributes and methods of objects"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""

    return dir(obj)

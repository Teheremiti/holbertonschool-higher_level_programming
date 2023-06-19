#!/usr/bin/python3
"""Module with a function to check if an object is an instance of
a class or one of its derivated classes"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a specified class or 
    one of its derivatives"""

    return isinstance(obj, a_class)

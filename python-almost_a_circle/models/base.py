#!/usr/bin/python3
"""Module defining the Base class"""


class Base:
    """Defines the attributes and methods of the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for the Base class.

        Args:
            id (int): Positive integer to set class instance's id to.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#!/usr/bin/python3
"""Module defining the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the attributes and methods of the Square class that inherits
    from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method for the Square class.

        Args:
            size (int): Determines the size of a Square instance
            x (int): Position of the square on the x axis
            y (int): Position of the square on the y axis
            id (int): id of the Square instance
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines the string representation of a Square object"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

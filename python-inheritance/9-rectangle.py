#!/usr/bin/python3
"""Module where the Rectangle class is defined"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the Rectangle class which inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the object's attributes during instanciation

        Args:
            width (int): Defines the width of the object
            height (int): Defines the height of the object
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Computes and returns the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

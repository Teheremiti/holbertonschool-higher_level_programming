#!/usr/bin/python3
"""Module with a Square class that defines more attributes"""


class Square:
    """Class to define a square of a given size"""
    def __init__(self, size=0):
        """Initialize a square to a given size.

        Args:
            size (int, optional): Size of the square.
                Defaults to 0. Stored as a private attribute

        Raises:
            TypeError: If the size attribute is not an integer.
            ValueError: If the size attribute is less than zero.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute the area of a square of size 'size'.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        The value must be an integer greater than 0.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print out a square with the char '#' of the size determined by the
        '__size' attribute."""

        if self.__size > 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()

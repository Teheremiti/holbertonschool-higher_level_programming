#!/usr/bin/python3
"""Module with a Square class that defines more attributes"""


class Square:
    """Class to define a square of a given size and position"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square to a given size.

        Args:
            size (int, optional): Size of the square.
                Defaults to 0. Stored as a private attribute
            position(tup, optional): Tuple representing the spacial
                position of the square. Defaults to 0. Stored as a private attribute

        Raises:
            TypeError: If the size attribute is not an integer.
            ValueError: If the size attribute is less than zero.
        """

        self.position = position
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

    @property
    def position(self):
        """Get the position in the plan of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of a square.

        The value must be a tuple of two positive integers.

        Raises:
            TypeError: If the position is not a tuple of two positive integers.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """Print out a square with the char '#' of the size determined by the
        '__size' attribute."""

        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()

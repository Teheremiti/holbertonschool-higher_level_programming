#!/usr/bin/python3
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

#!/usr/bin/python3
"""Module with a function to append a string to a text file"""


def append_write(filename="", text=""):
    """Appends the string 'text' to the end of the file

    Args:
        filename (str): File to append the content of 'text' to
        text (str): String to append at the end of the file

    Returns:
        The number of characters written
    """

    with open(filename, 'a') as f:
        return f.write(text)

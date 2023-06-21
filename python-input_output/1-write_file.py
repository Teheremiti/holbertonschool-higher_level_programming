#!/usr/bin/python3
"""Module with a function to write a string text into a file"""


def write_file(filename="", text=""):
    """Writes into a file. Creates the file if it doesn't exist, overwrites it
    otherwise.

    Args:
        filename (str): Name of the file to write in
        text (str): String to write the content of in the file
    """

    with open(filename, 'w') as f:
        return f.write(text)

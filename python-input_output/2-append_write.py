#!/usr/bin/python
"""Module with a function to append a string to a text file"""


def append_write(filename="", text=""):
    """Appends the string 'text' to the end of the file"""

    with open(filename, 'a') as f:
        return f.write(text)

#!/usr/bin/python3
"""Module with a function to read a file"""


def read_file(filename=""):
    """Reads a text file in utf-8 and prints its content to stdout"""

    with open(filename) as f:
        for line in f:
            print(line, end='')

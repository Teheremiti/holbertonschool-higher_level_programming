#!/usr/bin/python3
"""Module with a function to write an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation

    Args:
        my_obj (unknown): Object to write in the file as JSON
        filename  (file): File to write the JSON representation of my_obj in
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)

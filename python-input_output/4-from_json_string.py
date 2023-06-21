#!/usr/bin/python3
"""Module with a function that returns an object represented
by a JSON string"""


import json


def from_json_string(my_str):
    """Returns the object represented by the JSON string 'my_str'"""

    return json.loads(my_str)

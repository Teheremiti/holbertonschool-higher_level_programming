#!/sur/bin/python3
"""Module with a function that checks if an object is an instance of a class
that inherited from the specified class"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited(directly or
    indirectly) from the specified class"""

    my_class = type(obj)
    return (issubclass(my_class, a_class) and my_class is not a_class)

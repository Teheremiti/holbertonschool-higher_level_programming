#!/usr/bin/python3
def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int or float): Number to add. Casted into an integer if float.
        b (int or float): Other number to add. Casted into an integer if float.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: if a or b is not an integer.
    """

    try:
        return int(a + b)

    except Exception:
        if type(a) is not int:
            raise TypeError("a must be an integer")
        if type(b) is not int:
            raise TypeError("b must be an integer")

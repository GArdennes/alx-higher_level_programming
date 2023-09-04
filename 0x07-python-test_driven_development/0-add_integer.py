#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds 2 integers

    Args:
        a: The first integer
        b: The second integer. Defaults to 98

    Returns:
        The addition of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

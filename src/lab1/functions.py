def printMyString():
    print("myString")


def is_unique(x):
    """Checks that x has no duplicates.

    Args:
        x (table): A table to test

    Returns:
        Boolean: true if x has no duplicates
    """
    return len(x) == len(set(x))


def triangle_shape(height):
    """Function that generates a triangle of given height

    Args:
        height (int): Height of the triangle

    Returns:
        string: Representation of the triangle
    """

    str = ""
    for i in range(1, height + 1):
        prefix = "\n" if i > 1 else ""
        spaces = " " * (height - i)
        str += prefix + " " * (height - i) + "x" * (2 * (i - 1) + 1) + spaces
    return str

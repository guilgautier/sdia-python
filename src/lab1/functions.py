def is_unique(x):
    """Returns True if there is no duplicate in x otherwise return False.

    Args:
        x (list) : collection of elements

    Returns:
        boolean: True/False to know if there is duplicates

    """

    for value in x:
        if x.count(value) > 1:
            return False
    return True


def is_unique2(x):
    """Returns True if there is no duplicate in x otherwise return False.

    Args:
        x (list): collection of elements

    Returns:
        Boolean
    """

    return len(set(x)) == len(x)


def triangle_shape(height):
    """Returns a string that forms a triangle with height prescribed by `height`, or '' if height=0

    Args:
        height (int): height of the pyramid

    Returns:
        str: Representation of a pyramid
    """

    pyramid = ""
    if height == 0:
        return pyramid
    for i in range(height):
        pyramid += (
            (height - i - 1) * " " + (2 * i + 1) * "x" + (height - i - 1) * " " + "\n"
        )
    return pyramid[:-1]

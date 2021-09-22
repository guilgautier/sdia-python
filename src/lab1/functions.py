def is_unique(x):
    """returns True if the there is no duplicate items otherwise return False.
    Args:

    """
    for value in x:
        if x.count(value) > 1:
            return False
    return True


def triangle_shape(height):
    """returns a string that forms a triangle with height prescribed by `height`, or "" if height=0

    Args:
        height (int): height of the pyramid
    """
    pyramid = ""
    if height == 0:
        return pyramid
    for i in range(height):
        pyramid += (
            (height - i - 1) * " " + (2 * i + 1) * "x" + (height - i - 1) * " " + "\n"
        )
    return pyramid

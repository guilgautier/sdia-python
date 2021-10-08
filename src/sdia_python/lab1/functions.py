def is_unique(x):
    """Check that ``x`` has no duplicate elements.

    Args:
        x (list): elements to be compared.

    Returns:
        bool: True if ``x`` has duplicate elements, otherwise False
    """
    return len(set(x)) == len(x)


def triangle_shape(n, fillchar="x", spacechar=" "):
    """Return a string made of ``fillchar`` and ``spacechar``representing a triangle shape of height ``n``.

    For n=0, return ``""``.

    .. testcode::

        from sdia_python.lab1.functions import triangle_shape
        print(triangle_shape(6, fillchar="x", spacechar="_"))

    .. testoutput::

        _____x_____
        ____xxx____
        ___xxxxx___
        __xxxxxxx__
        _xxxxxxxxx_
        xxxxxxxxxxx

    Args:
        n (int): height of the triangle.
        fillchar (str, optional): Defaults to "x".
        spacechar (str, optional): Defaults to " ".

    Returns:
        str: string representation of the triangle.
    """
    width = 2 * n - 1
    return "\n".join(
        (fillchar * (2 * i + 1)).center(width, spacechar) for i in range(n)
    )

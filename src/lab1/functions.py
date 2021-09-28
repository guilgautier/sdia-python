def is_unique(x):
    """Tells if a there are duplicate items in a list or not

    Args:
        x (List): The list we check

    Returns:
        Boolean : True if there is no duplicate items in the list
    """
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] == x[j]:
                return False
    return True


def triangle_shape(height):
    """draw a triangle from a specific height

    Args:
        height (int): describe the height of the triangle

    Returns:
        String : shape of the triangle
    """

    t = ""
    if height <= 0:
        return t
    else:
        t = ""
        for i in range(1, height + 1):
            Ligne = ""
            for j in range(height - i):
                Ligne += " "
            for j in range(2 * i - 1):
                Ligne += "x"
            for j in range(height - i):
                Ligne += " "
            if i < height:
                Ligne += "\n"
            t += Ligne
        return t

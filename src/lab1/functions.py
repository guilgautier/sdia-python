def is_unique(x):
    """[ez]

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    return len(x) == len(set(x))


def triangle_shape(height):
    s = "x"
    esp = " "
    if height == 0:
        return ""
    return "\n".join(
        [
            (height - 1 - i) * esp + (2 * i + 1) * s + (height - 1 - i) * esp
            for i in range(height)
        ]
    )

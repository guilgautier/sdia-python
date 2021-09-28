def is_unique(x):
    while x != []:
        elt = x.pop()
        if elt in x: return False
    return True


def is_unique2(x):
    return len(x) == len(set(x))


def triangle_shape(n):
    """Do triangle shape in string

    Args:
        n (int): [description]

    Returns:
        [type]: [description]
    """

    base_n = 2 * n - 1
    res = []
    for i in range(1, n + 1):
        step_n = 2 * i - 1
        res.append(" " * ((base_n - step_n) // 2) + "x" * step_n + " " *
                   ((base_n - step_n) // 2))

    return "\n".join(res)

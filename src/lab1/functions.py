def is_unique(x):
    """[summary]

    Args:
        x ([type]): [ouooui]

    Returns:
        [type]: [description]
    """
    L = []
    verite = False
    for elem in x:
        verite = verite or (elem in L)
        L.append(elem)
    return not verite


def is_unique_bis(x):
    return len(set(x)) == len(x)


def triangle_shape(height):
    triangle = ""
    nbEspaces = height - 1
    for indice in range(height):
        triangle += nbEspaces * " "
        triangle += "x" * (indice * 2 + 1)
        triangle += nbEspaces * " "
        if indice < (height - 1):
            triangle += "\n"
        nbEspaces += -1
    return triangle

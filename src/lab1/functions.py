"""
Renvoie un booléen indiquant si la liste contient une seule fois chaque élément

Argument
x -- la liste
"""


def is_unique(x):

    M = []
    for value in x:
        if value not in M:
            M.append(value)
        else:
            return False
    return True


"""
Retourne une chaine vide si l'argument vaut 0, sinon retourne une chaine de caractère formant un triangle, avec une hauteur spécifiée par l'argument.

height -- la hauteur du triangle
"""


def triangle_shape(height):
    s = ""
    if height == 0:
        return s
    for k in range(0, height):
        if k != 0:
            s += "\n"
        t = ""
        for i in range(0, height - k - 1):
            t += " "
        for j in range(0, 2 * k + 1):
            t += "x"
        for i in range(0, height - k - 1):
            t += " "
        s += t
    return s

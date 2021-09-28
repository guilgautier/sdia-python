def is_unique(x):

    if len(x) == len(set(x)):
        return True
    else:
        return False


def triangle_shape(height):
    liste_print = []
    if height == 0:
        return ""
    else:
        for i in range(height):
            liste_print.append("x" * (2 * i + 1))
    print(*liste_print, sep="\n")

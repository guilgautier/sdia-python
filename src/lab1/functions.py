def is_unique(x):

    if len(x) == len(set(x)):
        return True
    else:
        return False


def triangle_shape(height):
    liste_print = []
    if height == 0:
        return ""
    if height == 1:
        return "x"
    if height == 2:
        return " x \nxxx"
    else:
        for i in range(height):
            if i != height - 1:
                liste_print.append(
                    " " * (height - i - 1)
                    + "x" * (2 * i + 1)
                    + " " * (height - i - 1)
                    + "\n"
                )
            else:
                liste_print.append(
                    " " * (height - i - 1) + "x" * (2 * i + 1) + " " * (height - i - 1)
                )
        return "".join(liste_print)


triangle_shape(3)

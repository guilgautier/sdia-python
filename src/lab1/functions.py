def is_unique(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] == x[j]:
                return False
    return True


def triangle_shape(height):
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
            t += Ligne + "\n"
        return t

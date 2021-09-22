def is_unique(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] == x[j]:
                return False
    return True


def triangle_shape(height):
    t = ""
    if height == 0:
        return t
    else:
        for i in range(height):
            l = ""
            for j in range(height):

                l += "x"
            l += "\n"
            t += l
        return t

def is_unique(x):

    if len(x) == len(set(x)):
        return False
    else:
        return True


def triangle_shape(height):
    if height == 0:
        return ""
    else:
        for i in range(height):
            print(" " * (height - 1 - i) + "x" * (2 * i + 1))

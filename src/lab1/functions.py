def printMyString():
    print("myString")


def is_unique(x):
    return len(x) == len(set(x))


def triangle_shape(height):
    str = ""
    for i in range(0, height):
        str += "\n" + " " * (height + 1 - i) + "x" * (2 * i + 1)
    return str

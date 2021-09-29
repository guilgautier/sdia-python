def is_unique(x):
    if x == []:
        return True
    else:
        y = x.pop()
        if y in x:
            return False
        else:
            return is_unique(x)


def triangle_shape(height):
    triangle = str()
    for i in range(height):
        for j in range(height - i - 1):
            triangle += " "
        for j in range(2 * i + 1):
            triangle += "x"
        for j in range(height - i - 1):
            triangle += " "
        if i != height - 1:
            triangle += "\n"
    return triangle

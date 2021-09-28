def is_unique(x):
    """[summary]

    Args:
        x (list of int]): [the list to test]

    Returns:
        [bool]: [show if there is not 2 same elements in x]
    """
    flag=True
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]==x[j]:
                 flag=False

    return flag

def triangle_shape(height):
    """[summary]

    Args:
        height ([int]): [the height of the triangle]

    Returns:
        [string]:[the triangle of x]
    """

    if height==0:
        return("")
    else:
        r=[(height-i-1)*" "+(2*i+1)*"x"+(height-i-1)*" "  for i in range(height)]



    return("\n".join(r))


# fonctionne à merveille





print(triangle_shape(3))

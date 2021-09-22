benco2000=1

def is_unique(x):
    """"x : list of integer"""
    for k in range(len(x)):
        for p in range(k+1,len(x)):
            if x[k]==x[p]:
                return (False)
    return (True)

def triangle_shape(height):
    """returns a string that forms a triangle of the height"""
    if height==0:
        return ("")
    else:
        elt=''
        for k in range(height):
            espace_avt=' '*(height-1-k)
            nb_x=str("x"*(2*k+1))
            elt=elt+espace_avt+nb_x+"\n"
        return(elt)

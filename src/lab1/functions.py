benco2000 = 'benco2000'



def is_unique(x):
    """salut"""
    if len(x)!= len(set(x)):
        return False
    else:
        return True



def triangle_shape(h):
    if h == 0:
        return("")
    else:
        for i in range (1,h):

            return((2*i+1)*"x")

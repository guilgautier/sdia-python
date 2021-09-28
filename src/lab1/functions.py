benco2000 = 'benco2000'



def is_unique(x):
    if len(x)!= len(set(x)):
        return False
    else:
        return True



def triangle_shape(h):
    n=h
    if h==0:
        print("")
    for i in range (0,h):
        print(' '*n, end='')
        print('x'*(2*i+1))
        n= n - 1

def is_unique(x):
    while x!=[]:
        elt  = x.pop()
        if elt in x: return False
    return True

def triangle_shape(n):
    base_n = 2*n-1
    for i in range(1, n):
        step_n = 2*i-1
        print(" " * ((base_n-step_n)//2) + "*"*step_n + " " * ((base_n-step_n)//2))

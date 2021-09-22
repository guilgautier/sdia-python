def is_unique(x):
    flag=True
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]==x[j]:
                 flag=False

    return flag

def triangle_shape(height):

    if height==0:
        return("")
    else:
        for i in range(height):
            print( (height-i)*" "+(2*i+1)*"x" + (height+i)*" "+"\n" )

triangle_shape(3)

from itertools import product

def itert():
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[a,b]

    return(str(" ".join(map(str,list(product(*c))))))
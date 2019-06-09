from itertools import permutations
from operator import itemgetter

def counterer():
    s,b=map(str,input().split())
    b=int(b)

    e=permutations(sorted(s),b)
    return(e)
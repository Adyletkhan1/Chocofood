import math
import os
import random
import re
import sys
from operator import itemgetter, attrgetter, methodcaller


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for i in range(n):
        arr.append([])
        arr[i]=list(map(int, input().split()))

    k = int(input())
    arr=sorted(arr,key=itemgetter(k))
    for j in range(n):
        print(" ".join(map(str,arr[j])))
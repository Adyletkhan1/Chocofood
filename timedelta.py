import math
import os
import random
import re
import sys
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt ='%a %d %b %Y %H:%M:%S %z'
    time1 = dt.strptime(t1, fmt)
    time2 = dt.strptime(t2, fmt)
    return int(abs((time1 - time2).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()

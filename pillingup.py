from itertools import groupby
from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    d = deque([int(x) for x,y in groupby(input().split())])
    for num in reversed(sorted(d)):
        if d[0] == num:
            d.popleft()
        elif d[-1] == num:
            d.pop()
        else:
            print('No')
            break
    else:
        print('Yes')

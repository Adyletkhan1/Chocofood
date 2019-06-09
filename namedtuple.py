from collections import namedtuple
N, Grade = int(input()), namedtuple('Grade', input())
Avg = sum(float(Grade(*input().split()).MARKS) for _ in range(N))/N
print ("%.2f" % Avg)

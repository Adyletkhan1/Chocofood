from itertools import product

num, m = map(int, input().split())
num_list = []
for i in range(num):
    num_list.append(sorted(list(map(int, input().split()))[1:]))
MAX = -1
for i in list(set(product(*num_list))):
    MAX = max(sum(map(lambda x: x**2, i))%m,MAX)
    if MAX == m-1:
        break
print(MAX)

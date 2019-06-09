from collections import OrderedDict
a = OrderedDict()

for _ in range(int(input())):
    b = input()
    a.setdefault(b, 0)
    a[b] += 1
   
print(len(a))
print(*a.values())
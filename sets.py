import cmath
def average():
    # your code goes here
    n = int(input())
    array = list(map(int, input().split()))
    array=set(array)
    return sum(array)/len(array)


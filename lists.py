N = int(input())
    ar=[]
    for _ in range(N):
        arr=input().split(' ')
        if(arr[0]=='insert'):
            ar.insert(int(arr[1]),int(arr[2]))
        if(arr[0]=='remove'):
            ar.remove(int(arr[1]))
        if(arr[0]=='append'):
            ar.append(int(arr[1]))
        if(arr[0]=='sort'):
            ar.sort()
        if(arr[0]=='print'):
            print(ar)
        if(arr[0]=='reverse'):
            ar.reverse()
        if(arr[0]=='pop'):
            ar.pop()
    
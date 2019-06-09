ar=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        ar.append([])
        ar[i]=[score,name]

    ar.sort()
    for i in range(1,len(ar)):
        if(ar[i][0]!=ar[0][0]):
            print(ar[i][1])
            for j in range(i+1,len(ar)):
                if(ar[j][0]==ar[i][0]):
                    print(ar[j][1])
            break  
        
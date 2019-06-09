def merge_the_tools():
   string, k = input(), int(input())
   n = len(string)
   for i in range(0,n,k):
        m = string[i:i+k]
        # print(m)
        M = []
        for j in range(len(m)):
            if m[j] not in M:
                M.append(m[j])
        return "".join(M)


    
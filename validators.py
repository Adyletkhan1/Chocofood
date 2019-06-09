if __name__ == '__main__':
    s = str(input())
    t=False
    for c in s:
        if(str(c).isalnum()):
            print(True)
            t=True
            break
    if(t==False):
        print(t)
    t=False

    for c in s:
        if(str(c).isalpha()):
            print(True)
            t=True
            break
    if(t==False):
        print(t)
    t=False

    for c in s:
        if(str(c).isdigit()):
            print(True)
            t=True
            break
    if(t==False):
        print(t)
    t=False

    for c in s:
        if(str(c).islower()):
            print(True)
            t=True
            break
    if(t==False):
        print(t)
    t=False

    for c in s:
        if(str(c).isupper()):
            print(True)
            t=True
            break
    if(t==False):
        print(t)
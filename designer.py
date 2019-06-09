a,b=map(int,input().split())

for i in range(0,a//2):
    print(((2*i+1)*".|.").center(b,"-"))
    
print("WELCOME".center(b,"-"))

for i in reversed(range(a//2)):
    print(((2*i+1)*".|.").center(b,"-"))
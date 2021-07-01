n=int(input())

for i in range(0,n+1):
    for k in range(n-i,0,-1):
        print(" ",end='')
        
    for j in range(0,i):
        print("*",end='')
    print()

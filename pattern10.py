n=int(input())

a=1

for i in range(1,n):
    a=1
    for j in range(1,n+1):
        if j%2!=0:
            
            print(a,end="")
            a=a+1
        else:
            print(i,end="")

        
    print()

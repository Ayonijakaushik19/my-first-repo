n=int(input())
s=[]

if n<2:
    print(n)
else:
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            s.append(i)
if len(s)==0:
    print(n)
else:
    for x in s:
        if n%x==0:
            print(x)

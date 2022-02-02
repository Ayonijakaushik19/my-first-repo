n=int(input())
i=n
while i<=n:
    if n%i==0:
        print(i)
    i-=1
    if i==0:
        break

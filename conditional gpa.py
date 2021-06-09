a=int(input())
b=int(input())
c=int(input())

if a<=0 or b<=0 or c<= 0:
    print("NO")
elif a**2==(b**2+c**2):
    print("YES")
elif b**2==(a**2+b**2):
    print("YES")
elif c**2==(a**2+b**2):
    print("YES")
elif a==b==c:
    print("No")
else:
    print("NO")

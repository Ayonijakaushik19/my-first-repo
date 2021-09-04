#factorial of a number
n=int(input())
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)
    
# another method    
n=int(input())
fact=1
if n<0:
    print("Not defined")
else:
    while (n>0):
        fact=fact*n
        n=n-1
    print(fact)    

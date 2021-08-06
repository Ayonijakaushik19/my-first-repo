#find LCM
n1=int(input())
n2=int(input())
maxi=0
if(n1==n2):
    print(n1,"LCM is",n1)
else:
    if n1<n2:
        maxi=n2
    if n2<n1:
        maxi=n1
for i in range(maxi,n1*n2):
    if (i%n1==0 and i%n2==0):
        print(i,"LCM is",i)
        break
else:
    print(n1*n2,"for two prime numbers")
    

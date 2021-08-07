#find HCF
n1=int(input())
n2=int(input())
mini=0
if(n1==n2):
    print(n1,"HCF is",n1)
else:
    if n1<n2:
        mini=n1
    if n2<n1:
        mini=n2
for i in range(mini,1,-1):
    if n1%i==0 and n2%i==0:
        print(i,"HCF is",i)
        break
else:
    print(1) # For Co-primes

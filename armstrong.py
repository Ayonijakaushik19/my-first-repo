#armstrong number
n=int(input())
#making a local copy
n1=n
sum=0
while n>0:
    digits=n%10
    n=n//10
    sum=sum+(digits**3)
if sum==n1:
    print("Hurray,we got an armstrong number")
else:
    print("Oops,try once again")

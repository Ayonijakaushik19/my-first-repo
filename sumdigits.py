#sum of digits
n=int(input())
n=abs(n)
sum=0
while(n>0):
    digits=n%10
    n=n//10
    sum=sum+digits
print(sum)    

#product of digits
n=int(input())
n=abs(n)
product=1
while(n>0):
    digits=n%10
    n=n//10
    product=product*digits
print(product)    

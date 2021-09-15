#product of digits of a number 
n=abs(int(input()))
product=1
if n==0:
    print("0")
else:
    while (n>0):
        
        digits=n%10
        n=n//10
        product*=digits
    print(product)

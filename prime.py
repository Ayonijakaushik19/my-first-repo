#prime number
num=int(input())
flag=True
if num==2:
    print("It is prime")
    
for i in range(3,num):
    if num%i==0:
        flag=False
        break
if flag==True:
    print("It is prime")
else:
    print("It is not prime")

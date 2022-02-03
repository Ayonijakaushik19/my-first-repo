#Accept a positive integer n as input, where n > 1.
#Print PRIME if n is a prime number and NOTPRIME otherwise.

n=int(input())
flag=0
for i in range(2,n//2+1):
    if n%i!=0:
        continue
    else:
        flag=1
        break
if flag==0:
    print("PRIME")
else:
    print("NOTPRIME")

#sum of all prime numbers between 1 and n

n=int(input())
sum=0
if (n>=2):
    sum+=2
for i in range(3,n+1):
    for j in range(2,i):
        if (i%j)==0:
            break
    else:
        sum+=i
print(sum)
            
            

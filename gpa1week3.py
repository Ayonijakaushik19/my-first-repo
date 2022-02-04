# Accept n as input and print sum of numbers as 1+(1+2)+(1+2+3)...

n=int(input())
sum=0

for i in range(1,n+1):
    for j in range(1,i+1):
        sum+=j
print(sum)
    

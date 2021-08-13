#printing a series
x=int(input())
n=int(input())
sum=1
for i in range(2,n+1):
    sum=sum+x**i
print(sum)

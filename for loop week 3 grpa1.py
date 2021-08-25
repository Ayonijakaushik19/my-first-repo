n=int(input())
sum=0

for i in range(1,n+1):
    k=i*(i+1)
#we are taking sum of first n natural numbers but
#one important thing that was twist in this question is that we are retaining the previous sum value into the term
#as for example if n=3
         #1+(1+2)+(1+2+3)
    k=k/2
    sum+=k
print(int(sum))
    

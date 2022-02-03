Accept a positive integer as input and print the sum of the digits in the number.

n=int(input())
quo=0
rem=0
sum=0
while(n>0):
    rem=n%10
    n=n//10
    sum+=rem
    
print(sum)    

#2 methods


pos_int=int(input())
pos_int=str(pos_int)
sum=0
for i in range(0,len(pos_int)):
    sum+=int(pos_int[i])
print(sum)

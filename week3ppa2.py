#sum of the digits


number=abs(int(input()))
sum=0
while(number>0):
    digits=number%10
    number=number//10
    sum+=digits
print(sum)

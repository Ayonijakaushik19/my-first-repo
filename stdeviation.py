import math
#step1
lst=[]
datapoints=str(input())


while datapoints!="END":
    lst.append(int(datapoints))
    datapoints=str(input())
#we have taken another input from user to check if it's equaal to "END"or not, or if she wants to give another input
#print(lst)

#step 2-to get the length of the list of data points that user have entered and also find the sum and average

length=0

length=len(lst)

sum=0
for x in lst:
    sum=sum+x
    
average=sum/length

#step 3-to find the summation of x[i]-x which is equal to lst[i]-average in my case
summation=0

for y in lst:
    summation+=(y-average)**2
    
#step4-to find the actual standard deviation

standard_deviation=summation/(length-1)
#we can use **0.5 also as power in the process of taking square root in place of math function

print(math.sqrt(standard_deviation))
print(round(math.sqrt(standard_deviation),2))





    

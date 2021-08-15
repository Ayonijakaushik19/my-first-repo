n1=int(input())
n2=int(input())
# n1 and n2 are same if they have equal number of digits in them
count1=0
count2=0
while n1>0:
    count1+=1
    n1=n1//10
#we can't alter range in for loop but here range is changing during change in n2,so we don't use for loop here
#n1 and n2 chota ho rha hai
while n2>0:
    count2+=1
    n2=n2//10
if count1==count2:
    print("Same number")
else:
    print("Not same number")
    
    

    
#But here it fails when one number is negative and another numebr is positive

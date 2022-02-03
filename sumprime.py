n=int(input())
sum=0

for i in range(2,n+1):
    flag=0
    for j in range(2,i//2+1):
        if (i%j) !=0:
            continue
        else:
            flag=1
            break
    if flag==0:
        sum+=i
   
print(sum)
        
            
        

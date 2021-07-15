n=int(input())
for i in range(0,n):
    for k in range(n-i,0,-1):
        print(" ",end='')       
    for j in range(0,i+1):
        print(n-i,end='')
    print()
        
#notice the pattern dependancy,,and the values dependency 
        

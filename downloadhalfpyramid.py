#print in downward half pyramid
n = int(input())  
# the outer loop is executing in reversed order  
for i in range(n, 0, -1):    
    for j in range(0, i-1 ): 
       # print(j)
        print("*", end=' ')  
    print(" ")  

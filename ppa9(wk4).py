n=int(input())
A=[]

for i in range(n):
    temp_list=list(map(int,input().split()))
    A.append(temp_list)
s=int(input()) 

for i in range(n):
    for j in range(n):
        A[i][j]*=s
        if j!=n-1:
            print(A[i][j],end=" ")
        else:
            print(A[i][j])
   
        

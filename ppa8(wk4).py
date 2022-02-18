n=int(input())
A=[[0 for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:
            A[i][j]=1
        if j!=n-1:
            print(A[i][j],end=",")
        else:
            print(A[i][j])
            

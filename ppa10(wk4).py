n=int(input())
A=[]
B=[]
C=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    temp_list=list(map(int,input().split(","))) 
    A.append(temp_list)
for j in range(n):
    tempo_list=list(map(int,input().split(",")))
    B.append(tempo_list)
    
for i in range(n):
    for j in range(n):
        C[i][j]=A[i][j]+B[i][j]
        
for i in range(n):
    for j in range(n):
        if j!=n-1:
            print(C[i][j],end=",")
        else:
            print(C[i][j])
        
  


        

    


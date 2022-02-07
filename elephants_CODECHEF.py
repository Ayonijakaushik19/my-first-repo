T=int(input())

while(T>0):
    T-=1
    
    input_list=list(map(int,input().split())) 
    N=input_list[0]
    C=input_list[1]
    
    candywant_list=list(map(int,input().split()))
    """ flag=True
    for i in range(len(candywant_list)):
        if (i+1<=candywant_list[i] or candywant_list[i]<=N) :
            
            N-=candywant_list[i]
            
            continue
        
        else:
            flag=False
            break
    if flag==True:
        print("Yes")
    else:
        print("No")"""
    
        
    if C>=sum(candywant_list):
        print("Yes")
    else:
        print("No")
            

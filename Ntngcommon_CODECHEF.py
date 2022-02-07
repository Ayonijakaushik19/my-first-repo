T=int(input())
while(T>0):
    T-=1 
    
    integer_list=list(map(int,input().split())) 
    
    N=integer_list[0]
    M=integer_list[1]
    
    Alice_list=list(map(int,input().split())) 
    Berta_list=list(map(int,input().split())) 
    
    throw_list = list(set(Alice_list) & set(Berta_list))
    
    
    print(len(throw_list))

# My first COMPETETIVE CODE

T=int(input())

while(T>0):
    T=T-1
    #Taking multiple inputs in one line in Python.Please check input sincerely.
    input_list = list(map(int,input().split())) 
    N=input_list[0]
    M=input_list[1]
    K=input_list[2]
    
    ignored_list = list(map(int,input().split())) 
    #Already making a list so no need to loop through for and taking different inputs in different iteration  
    tracked_list = list(map(int,input().split())) 
    """N,M,K=int(input()),int(input()),int(input())
    ignored=[]
    tracked=[]
    
    for i in range(1,M+1):
        a=int(input())
        ignored.append(a)
    for j in range(1,K+1):
        b=int(input())
        tracked.append(b)"""
    # NO need to usee line 14 to 23        
    igtr=[]
    
    igtr= [value for value in ignored_list if value in tracked_list]
    # line 27-How to find intersection of two lists in python
    uniguntr=N-len(list(set(ignored_list) | set(tracked_list)))
    #line 29-How to find union without duplicates-set is removing duplicates from each list and append the both thereafter.
    
    print(len(igtr),uniguntr)
    
    
    #Thing to take account of:Input,Output,Constraint
    

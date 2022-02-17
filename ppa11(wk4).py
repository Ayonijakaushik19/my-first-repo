def solution(L):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
   
    sorted_L=[]
    for i in range(len(L)):
        max_index=0
        max=L[0]
        for j in range(len(L)):
            if max<L[j]:
                max=L[j]
                max_index=j
        sorted_L.append(max)
        L.pop(max_index)
    
        
    ### Enter your solution above this line
    return sorted_L

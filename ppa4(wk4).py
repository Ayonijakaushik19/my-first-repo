L = input().split(',')
max_len=L[0]
for i in range(len(L)):
    if len(L[i])>=len(max_len):
        max_len=L[i]
        #We are reassigning again and again even the words ARE OF EQUAL Length.
        #So ultimately it will be the rightmost word.
print(max_len)
    
    
        
    
    

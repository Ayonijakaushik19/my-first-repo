#This is the example of print simple pyramid pattern

n=int(input())

#outer loop to handle number of rows

for i in range(0,n):
    
    #inner loop to handle number of columns
    #values is changing according to outer loop
    
    for j in range(0,i+1):
        
        #printing stars
        print("*",end="")
        
    #ending line after each row
    print()



"""Accept a sequence of positive integers as input and print the maximum number in the sequence. 
The input will have n+1 lines, where n denotes the number of terms in the sequence. The i^{th}
line in the input will contain the i^{th}term in the sequence for 1≤i≤n. 
The last line of the input will always be the number 0.
Each test case will have at least one term in the sequence."""



last_line=0
maxi=0
a=1
while(a!=last_line):
    a=int(input())
    if a>maxi:
        maxi=a
    
print(maxi)
    

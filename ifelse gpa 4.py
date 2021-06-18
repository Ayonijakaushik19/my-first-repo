
str1 = input()
counts= [0,0,0,0,0] # here we are taking a list of flags that will signify whether the particular vowels exists in the srting or not 

if str1.count('a')!=0 or str1.count('A')!=0:
    counts[0]=1
if str1.count('e')!=0 or str1.count('E')!=0:
    counts[1]=1
if str1.count('i')!=0 or str1.count('I')!=0:
    counts[2]=1
if str1.count('o')!=0 or str1.count('O')!=0:
    counts[3]=1
if str1.count('u')!=0 or str1.count('U')!=0:
    counts[4]=1
    
if counts[0]==1:
    print('a', end ="")
if counts[1]==1:
    print('e',end ="")
if counts[2]==1:
    print('i',end ="")
if counts[3]==1:
    print('o',end ="")
if counts[4]==1:
    print('u', end ="")

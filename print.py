Accept a positive integer nn as input and print the first nn integers on a line separated by a comma.

n=int(input())
i=1
while (i<=n):
    if i!=n:
        print(i,end=",")
    else:
        print(i)
    i+=1

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:42:56 2021
@author: ayoni
"""
import math
n=int(input())
i=1
sum=0
while i<=n:
    f= math.factorial(i)
    
    print(f)
    i+=1
    sum+=f
    
    
average=sum/n   
print(average) 
    
"""to find the average of the sum of the factorial of 1 to n numbers   
    
    
    
    
    
    
    

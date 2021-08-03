 -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 12:31:23 2021
@author: ayonija
"""
import sympy
n=int(input())
i=1
count=0
while i<=n:
    if sympy.isprime(i):
        count+=1
        
        print(i)
    i+=1
print(count)
# for prime numbers
q=int(input())
m=1
count1=0
while m<=q:
    if sympy.isprime(m):
        m+=1
        continue
    else:
        count1+=1
        print(m)
    m+=1
    
print(count1)    
    
#for composite numbers        
        
        

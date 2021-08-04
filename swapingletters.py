# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 10:34:58 2021

@author: ayonija
"""

string=input()
a=len(string)

modified_string=""
for i in range(a):
    if string[i].isupper():
        modified_string+=string[i].lower()
    elif string[i].islower():
        modified_string+=string[i].upper()
    else:
        modified_string+=string[i]
print(modified_string)
    

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:15:45 2021
@author: ayoni
"""
label=input()
positions="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if len(label)==1:
    print(positions.index(label)+1)

else:
    print((26*(positions.index(label[0])+1))+positions.index(label[1])+1)
    

label1=int(input())

q=label1//26
q=q-1

r=label1%26
r=r-1
if q==-1:
    print(positions[r])
else:
    
    print(positions[q]+positions[r])

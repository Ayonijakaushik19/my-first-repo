# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:41:35 2021

@author: ayoni
"""
n=input()

matches_played=len(n)

print(matches_played)

matches_won=n.count("W")

print(matches_won)

first_won=n.find("W")

print(first_won)

if first_won==-1:
    print("Not won")
else:
    print("won")

three_match_streak=n.find("WWW")

if three_match_streak==-1:
    
    print("don't have any streak")
     
else:
    print("it has")
    


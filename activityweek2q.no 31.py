"""
Created on Sat Jul 24 14:27:15 2021
@author: ayoni
"""
"""We are taking start and end as input ,start from where the bishop starts walking and end from where it goes"""
start=input()
end=input()
pos="ABCDEFGH"

# Here we will considering position as horizontal positions


start_xaxis,start_yaxis=pos.index(start[0]),int(start[1])

end_xaxis,end_yaxis=pos.index(end[0]),int(end[1])
""" As for example,in (C3,E5)-C3 (start) and E5 (end).

 We are checking whether the magnitude of horizontal distance travelled by bishop is equal
 to magnitude of vertical distance or not"""
 
 # we are taking the absolute value because may be it goes from down to up and up to down
 
if abs(start_xaxis-end_xaxis)==abs(start_yaxis-end_yaxis):
    print("YES")
else:
    print("NO")
    
    
#So far,so good


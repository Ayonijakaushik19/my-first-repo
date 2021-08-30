x,y,z=int(input()) , int(input()) , int(input())
if x+y==z:
   print('good triplet')
elif y+z==x:
    print('good triplet')
elif x+z==y:
    print('good triplet')
else:
    print('bad triplet')
 
 
#2nd way:
 
    
x,y,z=int(input()),int(input()),int(input())
if x+y==z or y+z==x or x+z==y:
    print('good triplet')
else:
    print('bad triplet')

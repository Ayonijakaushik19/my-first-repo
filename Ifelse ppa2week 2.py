x=float(input())
y=float(input())
if x>0 and y>0:
    print("I")
elif x<0 and y>0:
    print("II")
elif x<0 and y<0:
    print("III")
elif x>0 and y<0:
    print("IV")
elif x==0 and y!=0:
    print("Y-axis")
elif y==0 and x!=0:
    print("X-axis")
else:
    print("Origin") # to check if x and y are on origin
    

    

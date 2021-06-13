x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
if x1==x2:
    print("Vertical Line")
elif y1==y2:
    print("Horizontal Line")
else:
    m=(y2-y1)/(x2-x1)
    y3=((x3-x1)*(y2-y1))/(x2-x1)
    y3+=y1
    print(y3)
    if m>0:
        print("Positive Slope")
    else:
        print("Negative Slope")
        

    

    

    



    


bool_var=True
x=1
if bool_var:
    x=x+1 
    bool_var=not bool_var
#bool_var=false  
    if bool_var:#it's not saying that this bool_var (false) should be true,instead this whole if needs to be true.bool_var is the whole test. 
        x=x+1 
    else:
        x=x-1
print(x)  

Bool_var=False
y=8 
if Bool_var:
    y=y+5
    Bool_var=not Bool_var

    #Bool_var=True
    if Bool_var:
        y=y-1
    else:
        y=y+1 
print(y)        
    
    
    
    

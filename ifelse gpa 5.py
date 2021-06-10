Name1=str(input())
Dob1=str(input())
year1=int(Dob1[6:])
month1=int(Dob1[3:5])
date1=int(Dob1[0:2])

Name2=str(input())
Dob2=str(input())
year2=int(Dob2[6:])
month2=int(Dob2[3:5])
date2=int(Dob2[0:2])

if year1<year2:
    print(Name2)
elif year1==year2:
    if month1>month2:
         print(Name1)
    elif month1==month2:
        if date1>date2:
            print(Name1)
        elif date1==date2:
            if Name1>Name2:#lexical order (small comes first)string comparison
                print(Name2)
            else:
                print(Name1)
        else:
            print( Name2)
    else:
        print(Name2)
else:
    print(Name1)
             
        
            
            
       
           


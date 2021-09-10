T=int(input())

if T<0:
    print("INVALID")
elif T>=0 and T<=5:
    print("NIGHT")
elif T>=6 and T<=11:
    print("MORNING")
elif T>=11 and T<=17:
    print("AFTERNOON")
elif T>=18 and T<=23:
    print("EVENING")
elif T>=24:
    print("INVALID")
    
#we can also use "else" here.just wanted to check whether elif works alone or 
#is it really compulsory to write else after elif

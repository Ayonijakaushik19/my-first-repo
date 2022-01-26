# GRPA 1


a=int(input())
b=int(input())
c=int(input())
# We are combining the conditions using an "OR"operator
if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
    print("YES")
else:
    print("NO")


#GRPA 2


e1=int(input())
e2=int(input())
e3=int(input())
e4=int(input())
e5=int(input())

if (e1+e2)%2==0 or(e2+e3)%2==0 or(e3+e4)%2==0 or (e4+e5)%2==0 or (e5+e1)%2==0:
    print("YES")
else:
    print("NO")
    


#GRPA 3



name=input()
name1=name.lower()
vowels=""
if "a" in name1:
    vowels+="a"
if "e" in name1:
    vowels+="e"
if "i" in name1:
    vowels+="i"
if "o" in name1:
    vowels+="o"
if "u" in name1:
    vowels+="u"
#Check if vowels is non -empty
if vowels="":
    print="vowels"
else:
    print("none")

#GRPA 4




name1=input()
dob1=input()
name2=input()
dob2=input()
younger=""
#DD-MM-YYYY
if int(dob1[6:10])==int(dob2[6:10]):
    if int(dob1[3:5])==int(dob2[3:5]):
        if int(dob1[0:2])==int(dob2[0:2]):
            if name1>name2:
                younger=name2
            else:
                younger=name1
        elif int(dob1[0:2])>int(dob2[0:2]):
            younger=name1
        else:
            younger=name2
    elif int(dob1[3:5])>int(dob2[3:5]):
        younger=name1
    else:
        younger=name2
        
elif int(dob1[6:10])>int(dob2[6:10]):
    younger=name1
else:
    younger=name2
    
print(younger)



#GRPA 5



passwd=input()
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"

if (len(passwd)>=8 and len(passwd)<=32) and ( passwd[0]in upper or passwd[0] in lower) :
    if (("/" or "\\" or "=" or "'" or '"' or " ") not in passwd):
        print("True")
else:
    print("False")
    
    
















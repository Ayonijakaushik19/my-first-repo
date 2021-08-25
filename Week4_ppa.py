st = str(input())
x = st[len(st)//2] // st[2] -- u
print(x)
while x in st:
    st=st[:-1]  // string ko har bar reverse karke apne aap ko assign kiya gya jaise ayush ka hsuya ki usne first time 
    print(x,end="")
        
# st ka length - index of X in st     
# mere case m 5 tha X index 2 tha to mera X character 3 baar print hua 

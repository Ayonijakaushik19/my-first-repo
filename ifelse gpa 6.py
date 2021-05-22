s=str(input())
S1=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
S2=("abcdefghijklmnopqrstuvwxyz")

if len(s)<8 or len(s)>32:
    print(False)
elif  s[0] not in S1 and s[0] not in S2:
    print(False)
elif  s.count("\"")>0 or s.count("/")>0 or s.count("=")>0 or s.count("'")>0 or s.count('"')>0 or s.count(' ')>0:   # to check special characters in my string which are not allowed
     print (False)
else:
     print (True)

    
     

s="abcdefghijklmnopqrstuvwxyz"
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print(s[-a:-len(s):-3])
print(s[::-b])
print(s[c:0:-3])
print(s[len(s):-d:-3])
print(s[:e:-3])
#[:e:-3]-,means starting from the reverse side(as it's -3) going upto ending index (e),which is  zero

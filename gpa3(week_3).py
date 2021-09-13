E1,E2,E3,E4,E5=int(input()),int(input()),int(input()),int(input()),int(input())

if (E1+E2)%2==0 or (E2+E3)%2==0 or (E3+E4)%2==0 or (E4+E5)%2==0 or (E5+E1)%2==0:
    print("YES")
else:
    print("NO")

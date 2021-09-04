n=1
while n<=50:
    if n%3 ==0 and n%5==0:
        print("foobar")
    elif n%3==0:
        print("foo")
    elif n%5==0:
        print("bar")
        
    n+=1
    print(n)

n=int(input())
if n%2!=0:
    print("Weird")
elif n%2==0:
    if n==range(2,6):
        print('Not Weird')
    elif n==range(6,21):
        print("Weird")
    elif n>20:
        print("Not Weird")
        
    

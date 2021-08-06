# number of prime numbers
first_number=3
last_number=100


for i in range(first_number,last_number):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        

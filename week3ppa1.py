#print all the numbers divisible by 12 and 13 between [1000,2000]

lower=1000
upper=2000
for i in range(lower,upper+1):
    if i%156==0:
        print(i)

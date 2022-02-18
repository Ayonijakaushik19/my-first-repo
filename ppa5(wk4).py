import math
real_list=list(map(float,input().split()))
for i in real_list:
    if i!=real_list[-1]:
        print(math.floor(i),end=",")
    else:
        print(math.floor(i))

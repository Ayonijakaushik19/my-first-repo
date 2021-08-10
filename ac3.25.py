n=int(input())
sum_series=0
term=1
count=0
for term in range(1,n+1):
    sum_series+=1/term
    count+=1
print("{0:.2f}".format(count/sum_series))

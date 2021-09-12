#program to find leap year 
year=int(input('enter the year:'))
if year%400==0:
    print('yes')
elif year%4==0 and year%100!=0:
    print('yes')
else:
    print("no")


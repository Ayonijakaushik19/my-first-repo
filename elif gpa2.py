
TIME=int(input())
if TIME<0:
    print("INVALID")
elif TIME>=0 and TIME<=5:
    print("NIGHT")
elif TIME<=11 and TIME >=6:
    print("MORNING")
elif TIME>=12 and TIME<=17:
    print("AFTERNOON")
elif TIME>=18 and TIME<=23:
    print('EVENING')
else:
    print("INVALID")

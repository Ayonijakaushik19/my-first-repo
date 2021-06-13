n=str(input())
l=len(n)
mid=l//2
if l%2==0:
    if n[l-1]=='.':
        n=n.replace(".","")
        print(n[mid-1:mid+2])
    else:
       n=n+"."
      
       print(n[mid-1:mid+2])
       
    

else:
    print(n[mid-1:mid+2])

lst=[]

n=int(input())
lst.insert(0,6)
lst.insert(1,7)
lst.insert(2,8)
lst.insert(1,9)
print(lst)
lst.remove(9)
lst.append(9)
lst.sort()
print(lst)
lst.pop()
lst.sort(reverse=True)
print(lst)

#pop is an inbuilt function

#question number 24
"""n=int(input())
q=str(n)
sum=int(q[0])+int(q[1])
print(sum)"""
"""n=int(input())
q=n%10
n=n//10
print(q+n)"""
#alternative way of question number 24

n=int(input())
q=n%100
thirddigit=q%10
q=q//10
n=n//100
print(thirddigit+q+n)

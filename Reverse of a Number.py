# Python program to reverse a number
num = int(input())
rev = 0

while(n > 0):
	a = num % 10
	rev = rev * 10 + a
	num = num // 10

print(rev)


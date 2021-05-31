# Function to return hcf of a and b
def hcf(a,b):
	# Everything divides 0
	if (b == 0):
		return a
	return hcf(b, a%b)

# Driver program to test above function
a = int(input())
b = int(input())
if(hcf(a, b)):
	print('GCD of', a, 'and', b, 'is', hcf(a, b))
else:
	print('not found')



# Resussion is a programming principal where you apply divide and rule on the problem until it reaches its simplest form, aka base case and by using base case/ simplest form we move back 

# In recussion we invoke the function with inside of the function.
# Following is an example of factorial recussion!



def recurPow(x):
	if x == 1:
		return 1
	else:
		return x * recurPow(x -1)


factorial = recurPow(4)

# print(factorial)

# The same power can be solves using iterative method

def iterPower(base, exp):

	result = 1
	while exp > 0:
		result *= base
		exp -= 1

	return result

pow = iterPower(2, 1)

print(pow)

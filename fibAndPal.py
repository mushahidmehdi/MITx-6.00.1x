

# Fibonacci sequence!

def fibonacci(n):
	
	if n == 0 or n == 1:
		return 1

	else:
		return fibonacci(n-1) + fibonacci(n-2)


fib = fibonacci(10)

#print(fib)

# Palindrimic Sequence

def isPalindromic(x):

	def is_char(x):
		x = x.lower()
		letters = 'abcdefghijkmnopqrstuvwxyz'
		ans = ""
		for i in x:
			if i in letters:
				ans = ans + i

		return ans

	def compared_left_right(x):
		if len(x) <= 1:
			return True

		else:
			return x[0] == x[-1] and compared_left_right(x[1:-1])

	return compared_left_right(is_char(x))


string = "Able was I, ere I saw Elba"	
pal = isPalindromic(string)
print(pal)

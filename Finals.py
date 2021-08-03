# def sum_digits(s):
#    """ assumes s a string
#        Returns an int that is the sum of all of the digits in s.
#          If there are no digits in s it raises a ValueError exception. """
#    # Your code here
#	sum
#	for i in s:
#		if i is int():

def sum_digits(s):
	sum_int = 0

	for i in s:
		try:
			if type(int(i)) == int:
				sum_int += int(i)
		except:
			raise ValueError("Error")
	return sum_int


print(sum_digits('#'))
print(len(''))
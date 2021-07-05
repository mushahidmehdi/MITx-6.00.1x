# We want to write some simple procedures that work on dictionaries to return information.

# First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:

def how_many(aDict):

	values = list(aDict.values())
	print(values)
	newList = []

	for value in values:
		print(value)
		for val in value:
			print(val)
			newList.append(val)
	return len(newList)
			

aDict = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

#print(how_many(aDict))


# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

newDic = {'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}

def big(aDict):
	if aDict == "":
		return None
	temp = 0
	biggest = ""
	for k in aDict.keys():
		if len(aDict.get(k)) > temp:
			temp = len(aDict.get(k))
			biggest = k
	return biggest

print(big(newDic))
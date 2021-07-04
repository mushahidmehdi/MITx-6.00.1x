def oddTuples(aTup):
	'''
	aTup: a tuple
	returns: tuple, every other element of aTup. 
	'''
	newTup = []
	for i in range(len(aTup)):
		if i%2 == 0:
			newTup.append(aTup[i])
	return tuple(newTup)

print(oddTuples(('Hello', ',', 'World', '!', 'How', 'are', 'you', 'doing', 'today')))
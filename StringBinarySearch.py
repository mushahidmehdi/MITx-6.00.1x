def isIn(char, aStr):

	if aStr=='':
		return False
		
	if len(aStr)==1:
		return aStr == char

	midIndex = len(aStr)//2
	print(midIndex)
	midChar = aStr[midIndex]
	print(midChar)
	
	if char == midChar:
		return True
	elif char < midChar:
		return isIn(char, aStr[:midIndex])
	else:
		return isIn(char, aStr[midIndex+1:])
		
print(isIn('a', ''))
print(isIn('r', 'jmmrsvwy'))
print(isIn('t', 'dfhhjllmppqrvxxyzz'))
print(isIn('i', 'jknpx'))
print(isIn('x', 'acdikklmmnopqrsuxyy'))
print(isIn('b', 'abbcilrz'))
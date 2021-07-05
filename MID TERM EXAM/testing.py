

# Problem 1-1

# Suppose x = "pi" and y = "pie". The line of code x, y = y, x will swap the values of x and y, resulting in x = "pie" and y = "pi".

#x = "pi"
#y = "pie"
#x, y = y, x

#print(x)  # must be  x = "pie"
#print(y)  # y = "pi"
# Anser True

# Problem 1-2
# Suppose x is an integer in the following code:
# For any value of x, all calls to f are guaranteed to never terminate.

from typing import Type


def f(x):
    while x > 3:
        f(x+1)

#print(f(5))

# Answer False for any value smaller than 3 this loop will never be executed therfore there is no way it will run forever.



# Problem 1-4
# Suppose you have two different functions that each assign a variable called x. Modifying x in one function means you always modify x in the other function for any x.
# False Function have local scope rather than global level scope therefore 



# Problem 1-5
#  The following code will enter an infinite loop for all values of i and j.
# False the given loop will run infiniate if only the value of i or n is potitive and the word all make the statement false.
#import random
#i = random.randint(-100, 100)
#j = random.randint(-100, 100)
#while i >= 0:
#	while j >= 0:
#		print(i, j)

#____________________________________________
# Problem 2-5
# Consider the code:

#L = [1,2,3]
#d = {'a': 'b'}
#def f(x):
    #return 3
#print(L[3])
#print(d['b'])
# print(int('abc'))
#for i in range(1000001, -1, -2):
    #print(f)

# Problem 2-6
# stuff  = ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"] => Found it
# stuff = ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad") => Found it
# stuff = [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ] => 
# stuff = ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], ) => 
# stuff = ["iQ"] => Found it
# stuff = "iQ" 
#for thing in stuff:
#    if thing == 'iQ':
#        print("Found it")


# def Square(x):
    #return SquareHelper(abs(x), abs(x))

# def SquareHelper(n, x):
    # if n == 0:
       # return 0
    # return SquareHelper(n-1, x) + x

# print(Square(10))  # Return a correct value
# print(Square(-10)) # This function will work for negative numbers.




def myLog(x, b):

	if x == b:
		return 1

	elif x < b:
		return 0

	else:
		return 1 + myLog(x/b, b)


#print(myLog(16, 2))
#print(myLog(15, 3))

def getSubLists(L, n):
	newList = []
	while (0 < n <= len(L)):
		newList.append(L[:n+1])
		getSubLists(L[1:n], n)

	return newList

#L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
#n = 4
# print(getSubLists(L, n))

def getSublists(L, n):
	list_of_sublists = [] 	
	for i in range(len(L)-n+1):
		list_of_sublists.append(L[i:i+n]) 
		#create sublists of length n for every i and adds this sublist to master sublist
	return list_of_sublists

#print(getSublists(L, n))



def flattenList(L):
    newList = []
    for i in L:
        if type(i) != type([]):
            newList.append(i)
        else:
            newList.extend(flattenList(i))
    return newList

List = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flattenList(List))
print(type(List))


def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    #YOUR CODE HER
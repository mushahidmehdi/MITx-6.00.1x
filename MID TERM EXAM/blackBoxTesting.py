# max of three black box testing

from os import PRIO_PGRP
from typing import NewType


def maxOfThree(a, b, c):
	if a > b:
		bigger = a
	else:
		bigger = b

	if c > bigger:
		bigger = c
	
	return bigger


#print(maxofThree(2,5,7))		# expected ans 7
#print(maxofThree(2,4,1))		# expected ans 4
# print(maxofThree(2,2,2))		# (boundary err)
#print(maxofThree(1,1,0))		# (boundary err)
#print(maxofThree(0,0,0))		# (boundary err)

# a options: 
#print(maxOfThree(2, -10, 100))	# 100
#print(maxOfThree(7, 9, 10))		# 10
#print(maxOfThree(6, 1, 5))		# 6
#print(maxOfThree(0, 40, 20))


def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   if len(set1) == 0:
      return set2
   elif set1[0] in set2:
      return union(set1[1:], set2)
   else:
      return set1[0] + union(set1[1:], set2)


#print('Test Suite A')  
#print(union('',''))
#print(union('','a'))
#print(union('','ab')) 
#print(union('a',''),)  
#print(union('a','b')) 
#print(union('c','ab'))
#print(union('de','')) 
#print(union('ab','c')) 
#print(union('cd','ab'))  

#print("Test Suite B")
#print(union('abc',''))  
#print(union('abc','a')) 
#print(union('abc','ab'))		
#print(union('abc','d'))  
#print(union('abc', 'abcd'))
#
#print("Test Suite C") 
#print(union('','abc'))
#print(union('a','abc'))
#print(union('ab','abc')) 
#print(union('abc','abc'))
#
#print("Test Suit D")
#print(union('','abc'))
#print(union('a','abc'))
#print(union('ab','abc'))
#print(union('d','abc'))


def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a) 


# print(rem(2, 5)) # 2
# print(rem(5, 5)) # 0
# print(rem(7, 5)) # None

def f(n):
	if n == 0:
		return 1
	else:
		return n * f(n-1)

#print(f(3)) 
#print(f(0))
#print(f(1))

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
        
# print(fancy_divide([0, 2, 4], 1))
# print(fancy_divide([0, 2, 4], 4))
# print(fancy_divide([0, 2, 4], 0))


def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")

# print(fancy_divide([0, 2, 4], 1))
# print(fancy_divide([0, 2, 4], 4))
# print(fancy_divide([0, 2, 4], 0))

def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
        
# print(fancy_divide([0, 2, 4], 1))
# print(fancy_divide([0, 2, 4], 4))
# print(fancy_divide([0, 2, 4], 0))

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
        
# print(fancy_divide([0, 2, 4], 0)) 

def fancy_divides(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
        


def fancy_divide(list_of_numbers, index):
	denom = list_of_numbers[index]
	return [simple_divide(item, denom) for item in list_of_numbers]

def simple_divide(item, denom):
	try:
		return item/denom
	except ZeroDivisionError:
		return 0

#print(fancy_divide([0, 2, 4], 0))
#print("Second List")
#print(fancy_divide([0, 2, 4], 1))
from ps4a import *


# wordList = loadWords()
# frequencyDict = getFrequencyDict(sequence)

# def getWordScore(word, n):
# 	word = word.lower()
# 	wordScore = 0
# 	for i in word:
# 		wordScore += SCRABBLE_LETTER_VALUES.get(i)
# 	wordScore *= len(word)
# 	if len(word) == n:
# 		wordScore += 50
# 
# 	return wordScore
# word = 'ipek'
# n = 4
# print(getWordScore(word, n))
# 

# def updateHand(hand, word):
# 
# 	word = word.lower()
# 	hand = hand.copy()
# 
# 	for char in word:
# 		hand[char] -= 1
# 	return hand
# 
# hand = {'i':3, 'p':4, 'k':6, 'e':1, 'm':1, 'u':3, 's':3, 'h':5, 'a':4, 'd': 4}
# word = 'IPEK'
# print(updateHand(hand, word))

def isValidWord(word, hand, wordList):
	
	chars = [char for char in word]
	

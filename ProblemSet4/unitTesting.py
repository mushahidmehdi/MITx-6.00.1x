from os import PRIO_PGRP
from ps4a import *


wordList = loadWords()
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


#def isValidWord(word, hand, wordList):
# 
# 	# Gurded Statement! 
# 	if not word in wordList:
# 		return False
# 
# 	wordFreq = getFrequencyDict(word)
# 	print(wordFreq)
# 	for char in wordFreq:
# 		if wordFreq[char] > hand.get(char, 0):
# 			return False
# 	
# 	return True


def play(hand, wordList, n):

	totalScore = 0
	handLength = calculateHandlen(hand)
	print(handLength)

	while handLength > 0:
		# Display the hand
		print("Current Hand:", end= ' ')
		displayHand(hand)

		playerInput = input("Enter word, or a '.' to indicate that you are finished: ").lower()

		if playerInput == '.':
			break

		else:
			if not isValidWord(playerInput, hand, wordList):
				print("Invalid word, please try again.")

			else:
				scoreEarned = getWordScore(playerInput, n)
				totalScore += scoreEarned
				print(str(playerInput) + " earned " + str(scoreEarned) + " points.", end=" ")
				print("Total: " + str(totalScore) + " points")
				hand = updateHand(hand, playerInput)
				handLength = calculateHandlen(hand)

	if playerInput == '.' or handLength == 0:
		return ("Total score: " + str(totalScore))



word = wordList[random.randint(0, len(wordList))]
n = len(word)
hand = dealHand(n)

print(play(hand, wordList, n))

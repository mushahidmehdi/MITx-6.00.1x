# This is a fastest way to find a squareroot of any number
# Here what we called it, NewtopRapson Algorithem

# Lets say we want to find the square root of 43

number = 43

# We will make a first guess by taking half of a number
guess = number/2

# Lets Check How many loops will it run!
runGuesses = 0

# How close the squreroot will be to the actual number
epsilon = 0.01


# Lets define a while loop

while abs(guess**2 - number) >= epsilon:

	runGuesses += 1

	guess = guess - (((guess**2) - number)/(guess * 2))


print("The Number of gusses while loop runs: " + str(runGuesses))

print("The Square root of "  + str(number) + " is " + str(guess))
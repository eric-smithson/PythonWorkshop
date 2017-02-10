from __future__ import print_function

import random
# function that checks number and returns feedback
def givefeedback(guessnum, actualnum):
	if(guessnum < actualnum):
		print('Too low'); 
		return False
	elif(guessnum > actualnum):
		print('Too high')
		return False
	else:
		print('You got it!')
		return True


# intro text
print('Welcome to my game called guess the number!, it\'s a number between 1 and 100')


# while loop
result = False
actualnum = random.randint(1,100)
numguesses = 0

while(result == False):
	print('Enter your guess: ', end = '')
	guess = input()
	numguesses += 1
	result = givefeedback(int(guess), actualnum)

print('That took you ' + str(numguesses) + ' guesses!')
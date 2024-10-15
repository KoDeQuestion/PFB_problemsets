#!/usr/bin/env python3

#Import sys module to use sys.argv! #Test with 0, 33, 50, 66

import sys
number = int(sys.argv[1]) 

#PythonPB2_Step9 Write first statement declaring your number.

print('Your number is',str(number) + '.')

#PythonPB2_Step3-9 Writing nested 'if' statements.

if number < 0:
	message = "It's negative." #Define the string with whatever quote puncation you don't need in the string itself.
	print(message)
elif number > 0:
	message = "It's positive"
	if number < 50:
		message2 = 'but smaller than 50.'
		if number % 2 == 0:
			message3 = 'It is an even number that is smaller than 50.' 
			print(message,message2,message3)
		else:
			message3 = 'What an odd duck.'
			print(message,message2,message3)
	elif number > 50:
		message2 = 'and bigger than 50 (what an absolute unit).'
		if number % 3 == 0:
			message3 = 'It is larger than 50 and divisible by 3.'
			print(message,message2,message3)
		else:
			print(message,message2)
	else:
		message2 = 'and nifty.'
		print(message,message2)
else:
	message = 'Your number equal to 0. Cake is a lie.'
	print(message)




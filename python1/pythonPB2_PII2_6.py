#!/usr/bin/env python3
import sys
number = int(sys.argv[1]) 
if number < 0:
	message = 'negative'
	print(message)
elif number > 0:
	message = 'positive'
	if number < 50:
		message2 = 'but smaller than 50.'
		if number % 2 == 0:
			message3 = 'it is an even number that is smaller than 50.' 
			print(message,message2,message3)
		else:
			message3 = 'and an odd duck.'
			print(message,message2,message3)
	else:
		message2 = 'and an absolute unit.'
		print(message,message2)
else:
	message = 'Number equal to 0. Cake is a lie.'
	print(message)




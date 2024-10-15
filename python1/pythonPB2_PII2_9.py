#!/usr/bin/env python3
import sys
number = int(sys.argv[1]) 
print('Your number is',str(number) + '.')
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
	if number > 50:
		message2 = 'and bigger than 50 (what an absolute unit)'
		if number % 3 == 0:
			message3 = 'it is larger than 50 and divisible by 3'
			print(message,message2,message3)
		else:
			print(message,message2)
	else:
		message2 = 'and an absolute unit.'
		print(message,message2)
else:
	message = 'Number equal to 0. Cake is a lie.'
	print(message)




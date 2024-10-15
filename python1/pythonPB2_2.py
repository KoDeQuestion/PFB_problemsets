#!/usr/bin/env python3
import sys
number = int(sys.argv[1]) 
if number < 0:
	message = 'negative'
	print(message)
elif number > 0:
	message = 'positive'
	print(message)
else:
	message = 'Number equal to 0. Cake is a lie.'
	print(message)




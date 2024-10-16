#!/usr/bin/env python3

##Python Problem Set 4 - Question 13:

import sys

min = int(sys.argv[1])
max = int(sys.argv[2])

#min=10 and 1
#max=5 and 10

if min < max:
	list = [num for num in range(min, max + 1)]
	num_it = iter(list)
	for num in num_it:
		print(num)
else:
	print(f"Error: Arguments given aren't 1:minimum and 2:maximum.")
	

#!/usr/bin/env python3

#Python Problem Set 4 - Question 8:

for num in range(100):
	print(num)

for num in range(100):
	num+=1
	print(num)

#Python Problem Set 4 - Question 9:

list_100ints = [1 + num for num in range(100)]
num_it = iter(list_100ints)
for num in num_it:
	print(num)



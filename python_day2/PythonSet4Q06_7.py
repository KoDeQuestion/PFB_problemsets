#!/usr/bin/env python3

#Python Problem Set 4 - Question 6:

import sys

list = [101,2,15,22,95,33,2,27,72,15,52]
newlist = []

for num in list:
	#determine if even, if even append to new list
	if num % 2 == 0:
		newlist.append (num)
	else:
		continue
	#if odd continue

print(newlist)

#Python Problem Set 4 - Question 7:

list = [101,2,15,22,95,33,2,27,72,15,52]
sorted = sorted(list, key=None, reverse=False)
print(sorted)
sum_e = 0
sum_o = 0

for num in sorted:
        #determine if even, if even append to new list
        if num % 2 == 0:
                sum_e += num
        else:
                sum_o += num #The order here mattered. num += sum_o does not work


print(f'Sum of even numbers: {sum_e}')
print(f'Sum of odd numbers: {sum_o}')











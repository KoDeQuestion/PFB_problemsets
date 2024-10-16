#!/usr/bin/env python3

#Python Problem Set 4 - Question 5:

import sys

# 1000! = n * (n - 1)(n - 2)(n - 3)...3*2*1

fac = []

n = 1000

while n > 0:
	fac.append(n)
	n-=1

#This was a waste of memory.
#We want to multiply each integer in our list to give the factorial product. Exact the integer from the list.

product = 1
n = 1000
while n > 0:
        #first time around
	product *= n 
        n-=1

print(product)
	

















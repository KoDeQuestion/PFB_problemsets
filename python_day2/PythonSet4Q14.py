#!/usr/bin/env python3

##Python Problem Set 4 - Question 14:

#Create a script: Use a for loop, user provided arguments, and logic:
# 
    #Get the user provided minimum (sys.argv[1]) and maximum (sys.argv[2]).
    #Print out only the odd numbers between (inclusive) the min and max.

import sys

min = int(sys.argv[1])
max = int(sys.argv[2])

#Tested with:
#min=1
#max=10

if min < max:
        list = [num for num in range(min, max + 1)]
        num_it = iter(list)
        for num in num_it:
                if num % 2 == 0:
                    continue
                else:
                    print(num)
else:
        print(f"Error: Arguments given aren't 1:minimum and 2:maximum.")
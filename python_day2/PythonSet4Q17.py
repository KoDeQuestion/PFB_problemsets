#!/usr/bin/env python3

##Python Problem Set 4 - Challenge Problems:

#

#Create a shuffled sequence (Fisher-Yates shuffle)

#    Use a for loop to perform the following procedure N times (N = length of seq)
#    Select a random position A with randrange()
#    Select a random position B with randrange()
#    Exchange the letters at list indices A and B
#    Print the final shuffled sequence
#    Remember to test your code with test data.

import sys
from random import *

#x = sys.argv[1]

seq = '123456'
n = len(seq)

#convert seq to list

#Generate the random index
#random_index = randrange(len(seq))
#print(random_index)

seq = '67898'
n = len(seq)
newlist = []
for _ in seq: #I'm not using the variable so _ is a stand in to still use the loop
    #Generate the random index
    random_indexA = randrange(1, n)
    print(f'random_indexA:{random_indexA}')
    random_indexB = randrange(1, n)
    print(f'random_indexB:{random_indexB}') #These are already defined positions
    #Find positions
    #pos_indexA = seq.find(str(random_indexA))
    #print(f'pos_indexA:{pos_indexA}')
    #pos_indexB = seq.find(str(random_indexB))
    #print(f'pos_indexB:{pos_indexB}')
    #print(f'Confirm Index Pos A is what we think it is:{seq[pos_indexA]}') #This confirmed that the pos_index actually gives the character at that position (i.e. random_index)
    #Replace A with B THIS DOES WORK
    newlist = list(seq)
    newlist[random_indexA] = seq[random_indexB]
    newlist[random_indexB] = seq[random_indexA]
    newseq = ''.join(newlist) #convert list to string
    print(f'This is the OG {seq}')
    print(f'This is the new seq {newseq}')
    #Swap A with B [IN ONE MOVE?]
    #seq[random_indexA],seq[random_indexB] = seq[random_indexB],seq[random_indexA]

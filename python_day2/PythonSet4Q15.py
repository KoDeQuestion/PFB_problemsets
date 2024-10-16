#!/usr/bin/env python3

##Python Problem Set 4 - Question 15:

#
    #Create a script:

    #Create a list with the following data: ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
    #Use a for loop to iterate through each element of this list
    #For each element in the list, print its length and sequence separated by a tab. The output should look like:


list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in list:
    print(f'{len(seq)}\t{seq}')

#Modify: to also also print out the number (postion in the list) of each sequence.
#Make sure your columns are tab separated (i.e., "1\t4\tACGT\n")

#for index, seq in enumerate(list):
#    print(f'{len(seq)}\t{seq}\tPosition:{index}')

for index, seq in enumerate(list):
    print(f'Position:{index + 1}\t{len(seq)}\t{seq}')
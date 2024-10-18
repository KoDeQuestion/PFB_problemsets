#!/usr/bin/env python3

###Python Problem Set 6

##Q10 Part 2:

import sys

geneIDs_1 = sys.argv[1]
geneIDs_2 = sys.argv[2]

#Ensure the right number of files are given in command line
if len(sys.argv) < 3:
    print("Usage: python script.py <filename> <filename>")
    sys.exit(1)


stm_set = set()
tf_set = set()

with open(geneIDs_1,"r") as RS102:
    for line in RS102:
        line = line.rstrip() #remove the \n from the end of each line
        stm_set.add(line)

with open(geneIDs_2,"r") as RS104:
    for line in RS104:
        line = line.rstrip() #remove the \n from the end of each line
        tf_set.add(line)

tf_set.remove('Gene stable ID')
stm_set.remove('Gene stable ID')


print(f'The genes that are both stem cell proliferation genes and transcription factor genes are: {tf_set & stm_set}')

##Do it all in command line:
# sort <file1> > <sorted_file1>
# sort <file2> > <sorted_file2>
# comm -12 <sorted_file1> <sorted_file2> 
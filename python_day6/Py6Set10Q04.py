#!/usr/bin/env python3

###Python Problem Set 10: Functions


#Q4: Modify your script so that it can take two command line arguments:

#     FASTA file name
#     Max length of each line

# The script should reformat every sequence in the file to the specified max line length. Make sure your output is in proper FASTA format.

import sys
import re

file = sys.argv[1]
width = int(sys.argv[2])

def fasta_parser(file):
    fasta_dic ={}
    gene_header = ''
    with open(file,"r") as Read1:
        for line in Read1:
            #split based on the tab deliminator
            line = line.rstrip() #remove the \n from the end of each line
            matches = re.search(r'^>(\S+).*$', line) #We're already iterating in the for loop
            #so we don't need to use finditer in this case. We could use match, but search is more
            #flexible in general.
            if matches is not None: #This describes if Headers are found/True
                gene_header = matches.group(1)
                fasta_dic[matches.group(1)] = ''
            else:
                fasta_dic[gene_header] += line #+= to append! Not Overwrite!
    return fasta_dic

def char60_smarter(dna, char, linelen):
    #Insert char every 60 characters
    #for line in dna:
        #line = line.strip() #THIS DIDN'T WORK FOR \N EMBEDDED INSIDE STRINGS
    no_new_lines = dna.replace("\n","")
    linelen = int(linelen)
    return char.join(no_new_lines[i:i+linelen] for i in range(0, len(no_new_lines), linelen))

fasta_dic = fasta_parser(file)

#output_dic = {}

for gene in fasta_dic:
    dna = fasta_dic[gene]
    formatted_dna_4 = char60_smarter(dna, "\n", width)
    #print(repr(f'Q4:{char60_smarter(dna, "\n", width)}'))
    #print(f'Q4:{char60_smarter(dna, "\n", width)}')
    print(f'>{gene}:\n{char60_smarter(dna, "\n", width)}')
    #output_dic[gene] = formatted_dna_4
    

#print(output_dic)
#!/usr/bin/env python3

###Python Problem Set 10: Functions

#Q1: Create a function to format a string of DNA so that each line is no more than 60 nt long. Your function will:

    # INPUT: a string of DNA without newlines
    # OUTPUT: a string of DNA with lines no more than 60 nucleoties long

# INPUT:

# OUTPUT: 
# GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTT
# CTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTT
# GCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCA
# GACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
# TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTC
# CCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATG
# GTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGT
# GGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
# GTCATCTTCT



# def char60(dna, char):
#     #Give function a name, parameter - DNA
#     #Insert \n every 60 characters, starting with [61]
#     return char.join(dna[i:i+60] for i in range(0, len(dna), 60)) #Reformatted DNA string

def char60(dna, char):
    # Insert char every 60 characters
    return char.join(dna[i:i+60] for i in range(0, len(dna), 60))





dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'



formatted_dna = char60(dna, '\n')
print(formatted_dna)
print(repr(formatted_dna)) #This lets you visualize the newline chars


#Q2: Modify your function so that it will work whether the DNA string does or does not have newlines.

import re
def char60_smart(dna, char):
    # Insert char every 60 characters
    #for line in dna:
        #line = line.strip() #THIS DIDN'T WORK FOR \N EMBEDDED INSIDE STRINGS
    no_new_lines = dna.replace("\n","") 
    return char.join(no_new_lines[i:i+60] for i in range(0, len(no_new_lines), 60))

#INPUT:
dna_n = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

formatted_dna_n = char60_smart(dna_n, '\n')
formatted_dna = char60_smart(dna, '\n')
print(repr(f'{formatted_dna_n}'))
print(formatted_dna_n)

#Q3: Modify your function so that it takes two arguments, the DNA string and the max length of each line.

import re
def char60_smarter(dna, char, linelen):
    # Insert char every 60 characters
    #for line in dna:
        #line = line.strip() #THIS DIDN'T WORK FOR \N EMBEDDED INSIDE STRINGS
    no_new_lines = dna.replace("\n","")
    linelen = int(linelen)
    return char.join(no_new_lines[i:i+linelen] for i in range(0, len(no_new_lines), linelen))

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
width = 80

print(f'Q3:{char60_smarter(dna, "\n", width)}')

#Q4: Modify your script so that it can take two command line arguments:

#     FASTA file name
#     Max length of each line

# The script should reformat every sequence in the file to the specified max line length. Make sure your output is in proper FASTA format.

import sys
import re

file = sys.argv[1]

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
    # Insert char every 60 characters
    #for line in dna:
        #line = line.strip() #THIS DIDN'T WORK FOR \N EMBEDDED INSIDE STRINGS
    no_new_lines = dna.replace("\n","")
    linelen = int(linelen)
    return char.join(no_new_lines[i:i+linelen] for i in range(0, len(no_new_lines), linelen))

fasta_dic = fasta_parser(file)
for gene in fasta_dic:
    dna = fasta_dic[gene]
    width = 80
    formatted_dna_4 = char60_smarter(dna, "\n", width)
    #print(repr(f'Q4:{char60_smarter(dna, "\n", width)}'))
    print(f'Q4:{char60_smarter(dna, "\n", width)}')

#Q5: Create a new function that calculates the GC content of a DNA sequence.

    # it will take a DNA sequence without spaces and no header as an argument and return the percentage of nucleotides that are a G or C.
    # example percentGC = gc_conent('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA') or percentGC = gc_content(dna)

def percentGC(dna):
    c_count = dna.count('C')
    g_count = dna.count('G')
    dna_len = len(dna)
    gc_content = (c_count + g_count)/dna_len
    return gc_content

print(f'Q5:{percentGC(dna):.1%}')

#Q6: Create a new function that computes and returns the reverse complement of a sequence

    # it will take a DNA sequence without spaces and no header as an argument and return the reverse complement, with no spaces and no header.
    # example revComp_sequence = get_reverse_complement(dna)

width = 80
dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

def char60_smarter(dna, char, linelen):
    # Insert char every 60 characters
    #for line in dna:
        #line = line.strip() #THIS DIDN'T WORK FOR \N EMBEDDED INSIDE STRINGS
    no_new_lines = dna.replace("\n","")
    linelen = int(linelen)
    return char.join(no_new_lines[i:i+linelen] for i in range(0, len(no_new_lines), linelen))

def RevComp(dna):
    seq_comp  = dna.upper().replace('A','t').replace('T','a').replace('C','g').replace('G','c')
    seq_revcomp = seq_comp[::-1]
    return seq_revcomp



print(f'Q6:{char60_smarter(RevComp(dna),"\n", width)}')
print(repr(f'Q6:{char60_smarter(RevComp(dna),"\n", width)}'))

#Q7: Pipelines:
# a. Create a script that runs a command with subprocess.run.
# b. Check the exit status
# c. If exit status is good, run a second command.
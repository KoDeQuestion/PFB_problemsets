#!/usr/bin/env python3

###Python Problem Set 7

##Q1: For Python_07_nobody.txt find every occurrence of 'Nobody' and print out the position.

import re

with open("Python_07_nobody.txt","r") as Q1R:
    for line in Q1R:
        for found in re.finditer(r'(Nobody)', line):
            nobody_pos = found.start(1)+1
            print(nobody_pos)

##Q2: For Python_07_nobody.txt substitute every occurrence of 'Nobody' with your favorite name
# and write an output file with that person's name (ex. Michael.txt).

with open("Python_07_nobody.txt","r") as Q2R, open("JT.txt", "w") as Q2W:
    for line in Q2R:
        new_line = re.sub(r"Nobody",r"JT", line)
        Q2W.write(new_line)

##Q3: Using pattern matching, find all the FASTA header lines in Python_07.fasta. Note that the format
# for a header in a FASTA file is a line that starts with a greater than symbol and is followed by some
# text (e.g. >seqName description where seqName is the sequence name or identifier. The identifier 
# cannot have spaces in it. The description that follows it can have spaces.)

with open("Python_07.fasta","r") as Q3R:
    for line in Q3R:
        for header in re.finditer(r'(^>\S+[\s\S]*\n$)', line):
            print(header.group(0))

##Q4: If a line matches the format of a FASTA header, extract the sequence name and description
# using sub patterns (groups).
# Print sequence information in this format: id:seqName desc:seqDescription

with open("Python_07.fasta","r") as Q4R:
    for line in Q4R:
        for header in re.finditer(r'^>(\S+)(.*)\n$', line):
            seq_name = header.group(1)
            seq_descript = header.group(2)
            print(f'id:{seq_name}\ndesc:{seq_descript}')

##Q5: Create a FASTA parser, or modify your FASTA parser from the previous problem set, to use
# regular expressions. Also make sure your parser can deal with a sequence that is split over 
# many lines.

gene_dic ={}
gene_hd = ''

with open("Python_07.fasta","r") as Q5R:
    for line in Q5R:
        line = line.rstrip() #remove the \n from the end of each line
        #If it has > it's a header
        matches = re.search(r'^>(\S+).*$', line) #We're already iterating in the for loop
        #so we don't need to use finditer in this case. We could use match, but search is more
        #flexible in general.
        if matches is not None: #This describes if Headers are found/True
            gene_hd = matches.group(1)
            gene_dic[matches.group(1)] = ''
        else:
            gene_dic[gene_hd] += line #+= to append! Not Overwrite!
    print(f'fastaDict = {gene_dic}')   


##Q6: The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotides.
# See the IUPAC table to identify the nucleotide possibilities for the R and Y. 
# Write a regular expression to find and print all occurrences of the site in the 
# following sequence: Python_07_ApoI.fasta

# R = A or G
# Y = C or T

# Restriction Site Code: [AG]AATT[CT]
line_count = 0
with open("Python_07_ApoI.fasta","r") as Q6R:
    for line in Q6R:
        line = line.rstrip() #remove the \n from the end of each line
        line_count += 1
        #If it has > it's a header
        header_match = re.search(r'^>(\S+).*$', line) #We're already iterating in the for loop
        #so we don't need to use finditer in this case. We could use match, but search is more
        #flexible in general.
        if header_match is True:
            continue
        else:
            seq_match = re.search(r'([AG]AATT[CT])', line)
            if seq_match is None:
                continue
            else:
                print(f'For Line {line_count} there is a match: {seq_match.group(0)}')

##Q7: Determine the site(s) of the physical cut(s) by ApoI in the above sequence.
# Print out the sequence with "^" at the cut site.
# So first we need the Index position of the [AG]
# Second we need to insert a ^ at Index position +1

# line_count = 0
# with open("Python_07_ApoI.fasta","r") as Q7R:
#     for line in Q7R:
#         line = line.rstrip() #remove the \n from the end of each line
#         line_count += 1
#         #If it has > it's a header
#         header_match = re.search(r'^>(\S+).*$', line) #We're already iterating in the for loop
#         #so we don't need to use finditer in this case. We could use match, but search is more
#         #flexible in general.
#         if header_match:
#             continue
        
#         matches = re.search(r'(([AG])AATT[CT])', line)
#         if matches:
#             #seq_match_pos = seq_match.group(1) #Give the starting index
#             #Add ^ at starting index +1
#             line = re.sub(r"([AG])AATT([CT])",r"\1^AATT\2", line)
#             print(f'For Line {line_count} there is a match: {line}')
#This works, but not 100% -- it treats each line of sequence as an individual line, and will not 
#elements that wrap around.

gene7 ={}
gene_hd = 'x'
with open("Python_07_ApoI.fasta","r") as Q7R:
    for line in Q7R:
        #split based on the tab deliminator
        line = line.rstrip() #remove the \n from the end of each line
        #If it has > it's a header
        if line.startswith(">"): ###FOR THE FIRST TIME
        #if line.find(">"): THIS WAS ALWAYS TRUE, WHEN NOT FOUND
        #-1 IS STILL TRUE.
            gene_hd = line
            gene7[line] = ''
        else:
            gene7[gene_hd] += line #+= to append! Not Overwrite!
 
#print(f'fastaDict = {gene7}')
for gene_hd in gene7:
    replaced = re.sub(r"([AG])AATT([CT])",r"\1^AATT\2", gene7[gene_hd])
    print(f'Editted {gene_hd}: {replaced}')

#This works for a FASTA file of ONE sequence. FIXED IT WITH THE NEW FOR LOOP - AMAZING.

##Q8: Now that you've done your restriction digest, determine the lengths of your fragments
# and sort them by length (in the same order they would separate on an electrophoresis gel).

print(replaced)

#Take: AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
#Turn: ["AAAAAAAAGACGT","CTTTTTTTAAAAAAAAGACGT","CTTTTTTT"]

# for match in re.finditer((r"(.*)\^(.*)\^"), replaced):
#     print("Frag:", match.group(2))
print(type(replaced))
frag_list = replaced.split('^')
print(frag_list)

#I want the length of every [index] in frag list
#or just to sort based on the length of each index.

sorted(frag_list, key=len)

print(f'The fragments sorted by length: {sorted(frag_list, key=len)}')

##Q9: Download this file: ftp://ftp.neb.com/pub/rebase/bionet.txt or
# download from our github. This file is contains a list of enzymes and 
# their cut sites. Create a script that reads this file to fill a
# dictionary with the enzymes paired with their recognition patterns. 
#Skip the top 10 header lines and be aware of how the columns are delimited. 
# You'll modify this script in the next question. 

import re
enz_dic = {}
line_count = 0
with open("bionet.txt","r") as Q9R:
    for line in Q9R:
        line = line.rstrip()
        if line_count < 10:
            line_count += 1
        # else:
        #     for match in re.finditer(r'(\w.*)\s*(\w.*)\n', line):
        #         enz_dic[match.group(1)] = match.group(2)
        else:
            #line_split = line.split(r'         ') #THERE ARE NO TABS line_split = line.split(r'\s{2,}')
            line_split = re.split(r'\s{2,}', line)
            enz_dic[line_split[0]] = line_split[-1]

print(line_split)
print(enz_dic)

#There is an empty empty line at the bottom of the file.
#MY CODE DOESN'T TAKE INTO ACCOUNT THAT THERE ARE MULTIPLE LINES WITH THE SAME
#ENZYME NAME - SO THE KEYS IN THE DICTIONARY WOULD BE OVERWRITTEN!!! THIS CAN BE MANAGED:

            # def create_enzyme_dict(filename):

            #     enzyme_file = open(filename, 'r')

            #     enzyme_dict = {}
            #     with enzyme_file as f:
            #         for line in enzyme_file:
            #         # discard lines that do not have a cut site specified
            #             if "^" in line:
            #                 line = line.rstrip()
            #                 matches = re.match(r'(.+?)\s{3,}(.+)', line)
            #                 # some enzymes have more than one site in file
            #                 # so we make a list

            #                 # if there is no list of patterns yet, make one
            #                 try:
            #                     len(enzyme_dict[matches.group(1)]) 
            #                 except KeyError: #SEE THIS SOLUTION
            #                     enzyme_dict[matches.group(1)] = []
            #                 enzyme_dict[matches.group(1)].append(matches.group(2))

            #     return(enzyme_dict)



##Q10: Modify your last script to take two command line arguments: 
#the name of an enzyme and a fasta file with a sequence to be cut. 
#Load a dictionary of enzyme names and cut sites from the code you developed 
#in question 9. If the enzyme is present in the dictionary, and can cut the sequence,
# print out:
# the sequence, annotated with cut sites
# the number of fragments
# the fragments in their natural order (unsorted)
# the fragments in sorted order (largest to smallest)

#Import name of enzyme, import fasta file
import sys
EnzName = sys.argv[1]
FastaFile = sys.argv[2]
EnzName_Present = EnzName in enz_dic
#enz_dic still exists from Q9
#First: Check enz_dic for key that matches EnzName:
if enz_dic[EnzName] in enz_dic is False:
    print(f'The enzyme is not in the dictionary.')
elif enz_dic[EnzName] in enz_dic is True:
    cut_site = enz_dic[EnzName]

#Second: Fasta Parser
gene10 ={}
gene_hd = 'x'
with open(sys,argv[2],"r") as Q10R:
    for line in Q10R:
        #split based on the tab deliminator
        line = line.rstrip() #remove the \n from the end of each line
        #If it has > it's a header
        if line.startswith(">"): ###FOR THE FIRST TIME
        #if line.find(">"): THIS WAS ALWAYS TRUE, WHEN NOT FOUND
        #-1 IS STILL TRUE.
            gene_hd = line
            gene10[line] = ''
        else:
            gene10[gene_hd] += line #+= to append! Not Overwrite!

#print(f'fastaDict = {gene10}')
#Now that the FASTA is parsed, we want to sub the VALUE in gene10 by the VALUE in
# enz_dic
for gene_hd in gene10:
    replaced = re.sub(r"([AG])AATT([CT])",r"\1^AATT\2", gene10[gene_hd])
    print(f'Editted {gene_hd}: {replaced}')
#Load Dictionary of enzyme names + cut sites
#Check if the SeqName matches Dictionary Key
#If SeqName matches Dictionary Key, take Value (Cut Site),
#and split Seq "string" and print it out.

##Too many variables.
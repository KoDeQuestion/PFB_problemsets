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

for match in re.finditer((r"(.*)\^(.*)\^"), replaced):
    print("Frag:", match.group(2))
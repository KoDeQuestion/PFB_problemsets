#!/usr/bin/env python3

###Python Problem Set 6

##Extra: Expand on the nucleotide composition exercise
# iterate over each line in this file (seqName\tsequence\n)

#     for each sequence:
#         calculate and store the count of each unique nucleotide character in a dictionary
#         report the name, total of each nucleotide count, and the GC content


#This combines Q4 and Q6

#     #Write a script that determines the unique characters in this sequence:
# AQ4Set = set('GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA')
# print(f'Q4 SetA has the following nucleotides: {AQ4Set}')

#     #iterate over each unique character and count the number found in the sequence
#     #store each count in a dictionary. example: nt_comp['A']=2
# seq = 'GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'
# nt_count = {}
# for nt in seq:
#     if nt in nt_count:
#         nt_count[nt]+= 1
#     else:
#         nt_count[nt] =1;
# print(f'For your sequence the nucleotide count is {nt_count}')   

#     #when you are done counting each character calculate and report the nucleotide composition and the GC content.
#     # sum_of_values(keyC+keyG) / sum_of_all_values
# print(f'The GC content of the sequence is {(nt_count['G'] + nt_count['C'])/(nt_count['G'] + nt_count['C'] + nt_count['A'] + nt_count['T']):.1%}')

#     #or just divide by len(seq)

# print(f'The GC content of the sequence is {(nt_count['G'] + nt_count['C'])/(len(seq)):.1%}')

gene_dic_challenge = {}
nt_count = {}
gene_nt_count = {}
with open("Python_06.seq.txt","r") as QChR:
    for line in QChR:
        #split based on the tab deliminator
        line = line.rstrip() #remove the \n from the end of each line
        gene_id,seq = line.split('\t') #split on \t
        gene_dic_challenge[gene_id] = seq
for gene in gene_dic_challenge: #write from the dictionary
    seq = gene_dic_challenge[gene]
    for nt in seq:    
        if nt in nt_count: #G
            nt_count[nt]+= 1
        elif nt is G:
        elif nt is T:
        elif nt is C:
        else:
            nt_count[nt] =1
    gene_nt_count[gene] = nt_count[nt]  #write to new dictionary
   
print(nt_count)
print(gene_nt_count)

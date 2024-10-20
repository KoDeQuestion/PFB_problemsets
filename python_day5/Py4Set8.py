#!/usr/bin/env python3

###Python Problem Set 8

##Q1: Take a multi-FASTA Python_08.fasta file from user input and calculate
# the nucleotide composition for each sequence. Use a datastructure to keep 
#count. Print out each sequence name and its compostion in this 
#format seqName\tA_count\tT_count\tG_count\tC_count

        # seqs[geneName][nucleotide]=count

        # seqs['geneA']['A'] = 2
        # seqs['geneA']['T'] = 3
        # seqs['geneA']['G'] = 3
        # seqs['geneA']['C'] = 1


        # seqs['geneB']['A'] = 1
        # seqs['geneB']['T'] = 5
        # seqs['geneB']['G'] = 2
        # seqs['geneB']['C'] = 2
import re
fasta_dic ={}
gene_header = ''
with open("Python_08.fasta","r") as Q1R:
    for line in Q1R:
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
#print(fasta_dic)
nt_comp ={'A':0,'T':0,'G':0,'C':0}
for gene in fasta_dic:
    seq = fasta_dic[gene]
    nt_comp ={'A':0,'T':0,'G':0,'C':0}
    nt_comp['A'] = seq.count('A')
    nt_comp['T'] = seq.count('T')
    nt_comp['G'] = seq.count('G')
    nt_comp['C'] = seq.count('C')
    fasta_dic[gene] = [seq, nt_comp]
print(fasta_dic)

for gene in fasta_dic:
    print(f'seqs[{gene}][A] = {fasta_dic[gene][1]['A']}')
    print(f'seqs[{gene}][T] = {fasta_dic[gene][1]['T']}')
    print(f'seqs[{gene}][G] = {fasta_dic[gene][1]['G']}')
    print(f'seqs[{gene}][C] = {fasta_dic[gene][1]['C']}\n\n') #Added new line characters so there are
    #spaces between the different genes when printed.

#This works! :)

#Q2: Write a script that takes a multi-FASTA file Python_08.fasta from user
# input and breaks each sequence into codons (every three nucleotides is a codon) 
#in just the first reading frame. Your output should look like this:
    # seq1-frame-1-codons
    # CAT GCT TGA GTC
#Write the output to a file called 'Python_08.codons-frame-1.nt'.
# import re
# fasta_dic ={}
# gene_header = ''
# with open("Python_08.fasta","r") as Q1R:
#     for line in Q1R:
#         #split based on the tab deliminator
#         line = line.rstrip() #remove the \n from the end of each line
#         matches = re.search(r'^>(\S+).*$', line) #We're already iterating in the for loop
#         #so we don't need to use finditer in this case. We could use match, but search is more
#         #flexible in general.
#         if matches is not None: #This describes if Headers are found/True
#             gene_header = matches.group(1)
#             fasta_dic[matches.group(1)] = ''
#         else:
#             fasta_dic[gene_header] += line #+= to append! Not Overwrite!
#print(fasta_dic)

for gene in fasta_dic:
    seq = fasta_dic[gene][0]
    #print(seq) #Check that we're returning the right value.
    codons = [[seq[i:i+3] for i in range(0, len(seq), 3)]] #Using List Comphrension
    nt_comp ={'A':0,'T':0,'G':0,'C':0}
    nt_comp['A'] = seq.count('A')
    nt_comp['T'] = seq.count('T')
    nt_comp['G'] = seq.count('G')
    nt_comp['C'] = seq.count('C')
    fasta_dic[gene] = [seq, nt_comp, codons]

#print(fasta_dic) #Check that it worked.
for gene in fasta_dic:
    print(f'[{gene}]-frame-1-codons\n{fasta_dic[gene][2]}\n\n')

# seq1-frame-1-codons
# CAT GCT TGA GTC

##Q3: Now produce codons in the first three reading frames for each sequence 
#and print out ids and sequence records for each frame and print to a file called
# 'Python_08.codons-3frames.nt'

for gene in fasta_dic:
    seq = fasta_dic[gene][0]
    #print(seq) #Check that we're returning the right value.
    frame1 = [[seq[i:i+3] for i in range(0, len(seq), 3)]] #Using List Comphrension
    frame2 = [[seq[i:i+3] for i in range(1, len(seq), 3)]] #Using List Comphrension
    frame3 = [[seq[i:i+3] for i in range(2, len(seq), 3)]] #Using List Comphrension
    nt_comp ={'A':0,'T':0,'G':0,'C':0}
    nt_comp['A'] = seq.count('A')
    nt_comp['T'] = seq.count('T')
    nt_comp['G'] = seq.count('G')
    nt_comp['C'] = seq.count('C')
    fasta_dic[gene] = [seq, nt_comp, frame1, frame2, frame3]

#print(fasta_dic) #Check that it worked.
for gene in fasta_dic:
    print(f'[{gene}]-frame-1-codons\n{fasta_dic[gene][2]}\n'
    f'[{gene}]-frame-2-codons\n{fasta_dic[gene][3]}\n'
    f'[{gene}]-frame-3-codons\n{fasta_dic[gene][4]}\n\n')

##Q4: Now reverse complement each sequence and print out all six reading frames to a
# file called 'Python_08.codons-6frames.nt'

for gene in fasta_dic:
    seq = fasta_dic[gene][0]
    #print(seq) #Check that we're returning the right value.
    frame1 = [[seq[i:i+3] for i in range(0, len(seq), 3)]] #Using List Comphrension
    frame2 = [[seq[i:i+3] for i in range(1, len(seq), 3)]] #Using List Comphrension
    frame3 = [[seq[i:i+3] for i in range(2, len(seq), 3)]] #Using List Comphrension
    
    nt_comp ={'A':0,'T':0,'G':0,'C':0}
    nt_comp['A'] = seq.count('A')
    nt_comp['T'] = seq.count('T')
    nt_comp['G'] = seq.count('G')
    nt_comp['C'] = seq.count('C')
    
    seq_comp  = seq.upper().replace('A','t').replace('T','a').replace('C','g').replace('G','c')
    seq_revcomp = seq_comp[::-1]
    frame4 = [[seq_revcomp[i:i+3] for i in range(0, len(seq_revcomp), 3)]] #Using List Comphrension
    frame5 = [[seq_revcomp[i:i+3] for i in range(1, len(seq_revcomp), 3)]] #Using List Comphrension
    frame6 = [[seq_revcomp[i:i+3] for i in range(2, len(seq_revcomp), 3)]] #Using List Comphrension

    fasta_dic[gene] = [seq, nt_comp, frame1, frame2, frame3, frame4, frame5, frame6]

#print(fasta_dic) #Check that it worked.
for gene in fasta_dic:
    print(f'[{gene}]-frame-1-codons\n{fasta_dic[gene][2]}\n'
    f'[{gene}]-frame-2-codons\n{fasta_dic[gene][3]}\n'
    f'[{gene}]-frame-3-codons\n{fasta_dic[gene][4]}\n'
    f'[{gene}]-frame-4-codons\n{fasta_dic[gene][5]}\n'
    f'[{gene}]-frame-5-codons\n{fasta_dic[gene][6]}\n'
    f'[{gene}]-frame-6-codons\n{fasta_dic[gene][7]}\n\n')


##Q5:Translate each of the six reading frames into amino acids. Create one file for which you print
# the six reading frames (Python_08.codons-6frames.nt) and one file for which you print the
# translation of the six reading frames (Python_08.translated.aa). Use the following translation table:

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

import re
for gene in fasta_dic:
    seq = fasta_dic[gene][0]
    genes = {}
    genes[gene]={}
    #print(seq) #Check that we're returning the right value.
    
    #This is for the codon frames of the nucleotide sequence
    frame1 = [seq[i:i+3] for i in range(0, len(seq), 3)] #Using List Comphrension
    frame2 = [seq[i:i+3] for i in range(1, len(seq), 3)] #Using List Comphrension
    frame3 = [seq[i:i+3] for i in range(2, len(seq), 3)] #Using List Comphrension
    
    #This is for the nucleotide content of the original seq
    nt_comp ={'A':0,'T':0,'G':0,'C':0}
    nt_comp['A'] = seq.count('A')
    nt_comp['T'] = seq.count('T')
    nt_comp['G'] = seq.count('G')
    nt_comp['C'] = seq.count('C')
    
    #This is for the reverse comp. codon frames
    seq_comp  = seq.upper().replace('A','t').replace('T','a').replace('C','g').replace('G','c')
    seq_revcomp = seq_comp[::-1]
    frame4 = [seq_revcomp[i:i+3].upper() for i in range(0, len(seq_revcomp), 3)] #Using List Comphrension
    frame5 = [seq_revcomp[i:i+3].upper() for i in range(1, len(seq_revcomp), 3)] #Using List Comphrension
    frame6 = [seq_revcomp[i:i+3].upper() for i in range(2, len(seq_revcomp), 3)] #Using List Comphrension

    #fasta_dic[gene] = [seq, nt_comp,[],[],[],[],[],[]]
    genes[gene]['seq']=seq
    genes[gene]['nt_comp']=nt_comp
    genes[gene]['frame1_codons']=frame1
    #fasta_dic[gene]['frame1_aa']=to be determined .....

    
    #This is for translating the codons
    frame_count=1 #for list style set to 2
    for frame in [frame1,frame2,frame3,frame4,frame5,frame6]:
        amino_acids = []
        for codon in frame:
            #print(index_count,codon)
            #match to translation_table
            amino_acid = translation_table.get(codon)
            #print(f'Before if:{amino_acid}')
            if amino_acid:
                #print(f'After if:{amino_acid}')
                amino_acids.append(amino_acid)
        #print(f'After all codons:{amino_acids}') 
        #fasta_dic[gene][frame_count] = [frame, amino_acids] #fasta_dic[gene][index_count] = 
        key=f'frame{frame_count}_aa'
        genes[gene][key]=amino_acids
        frame_count+=1
        

print(genes) #Check that it worked.

# with open("Python_08.codons-6frames.nt", "w") as Q1W:
#     for gene in fasta_dic:
#         Q1W.write(f'[{gene}]-frame-1-codons\n{fasta_dic[gene][2][0]}\n'
#         f'[{gene}]-frame-2-codons\n{fasta_dic[gene][3][0]}\n'
#         f'[{gene}]-frame-3-codons\n{fasta_dic[gene][4][0]}\n'
#         f'[{gene}]-frame-4-codons\n{fasta_dic[gene][5][0]}\n'
#         f'[{gene}]-frame-5-codons\n{fasta_dic[gene][6][0]}\n'
#         f'[{gene}]-frame-6-codons\n{fasta_dic[gene][7][0]}\n\n')

# with open("Python_08.translated.aa", "w") as Q2W:
#     for gene in fasta_dic:
#         Q2W.write(f'[{gene}]-frame-1-codons\n{fasta_dic[gene][2][1]}\n'
#         f'[{gene}]-frame-2-codons\n{fasta_dic[gene][3][1]}\n'
#         f'[{gene}]-frame-3-codons\n{fasta_dic[gene][4][1]}\n'
#         f'[{gene}]-frame-4-codons\n{fasta_dic[gene][5][1]}\n'
#         f'[{gene}]-frame-5-codons\n{fasta_dic[gene][6][1]}\n'
#         f'[{gene}]-frame-6-codons\n{fasta_dic[gene][7][1]}\n\n')

with open("Python_08.codons-6frames.nt", "w") as Q1W:
    for gene in genes:
        Q1W.write(f'[{gene}]-frame-1-codons\n{genes[gene]['frame1_codons']}\n\n')

with open("Python_08.translated.aa", "w") as Q2W:
    for gene in genes:
        Q2W.write(f'[{gene}]-frame-1-codons\n{genes[gene]['frame1_aa']}\n\n')

        
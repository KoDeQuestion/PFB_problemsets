#!/usr/bin/env python3

###Python Problem Set 6

##Question 1: 
    #Make a set using the two different syntaxes for creating a set myset = set() and myset2 = {}.

mySet = set('ATGTGGG')
mySet2 = {'ATGTGGG', 'NNNNN'}

print(f'mySet is {mySet}')
print(f'mySet2 is {mySet2}')


    #What is the difference?
        #One is a list of strings and one is a string. 
    #Does it matter which method you use?
        #Yes, one notation is for strings and the other is for making sets of a list.
    #How many items are in mySet and mySet2?

print(len(mySet))
print(len(mySet2))

##Question 2: Write a script that creates 2 sets using the collections of numbers below.
    #Find the intersection, difference, union, and symetrical difference between these two sets.

Set1 = {3, 14, 15, 9, 26, 5, 35, 9}
Set2 = {60, 22, 14, 0, 9, 9}

print(f'The difference is {Set1 - Set2}.')
print(f'The union is {Set1 | Set2}.')
print(f'The intersection is {Set1 & Set2}.')
print(f'The symetrical difference is {Set1 ^ Set2}.')

##Question 3: If you create a set using a DNA sequence, what will you get back? Try it with this sequence:

Seq_Set = set('GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTNNGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACX')
print(Seq_Set)

#Seq_Set2 = {'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTNNGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACX'}
#print(Seq_Set2)

##Question 4: Nucleotide Composition
    #Write a script that determines the unique characters in this sequence:
AQ4Set = set('GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA')
print(f'Q4 SetA has the following nucleotides: {AQ4Set}')

    #iterate over each unique character and count the number found in the sequence
    #store each count in a dictionary. example: nt_comp['A']=2
seq = 'GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'
nt_count = {}
for nt in seq:
    if nt in nt_count:
        nt_count[nt]+= 1
    else:
        nt_count[nt] =1;
print(f'For your sequence the nucleotide count is {nt_count}')   

    #when you are done counting each character calculate and report the nucleotide composition and the GC content.
    # sum_of_values(keyC+keyG) / sum_of_all_values
print(f'The GC content of the sequence is {(nt_count['G'] + nt_count['C'])/(nt_count['G'] + nt_count['C'] + nt_count['A'] + nt_count['T']):.1%}')

    #or just divide by len(seq)

print(f'The GC content of the sequence is {(nt_count['G'] + nt_count['C'])/(len(seq)):.1%}')

##Question 5: Write a script todo the following to Python_06.txt
    #Open and read the contents
    #Uppercase each line
    #Print each line to the STDOUT
with open("Python_06.txt","r") as Q6: #Open and read the contents
    for line in Q6:
        line = line.rstrip() #remove the \n from the end of each line
        line = line.upper() #Uppercase each line
        print(line)

##Question 6: Modify the script in the previous problem to write the contents to a new file called "Python_06_uc.txt"
with open("Python_06.txt","r") as Q6, open("Python_06_uc.txt","w") as Q7:
    for line in Q6:
        #line = line.rstrip() #remove the \n from the end of each line
        line = line.upper() #Uppercase each line
        Q7.write(line)

##Question 7: Open and print the reverse complement of each sequence in Python_06.seq.txt.
#Each line is the following format: seqName\tsequence\n. 
#Make sure to print the output in FASTA format including the sequence name and a note in the description that this is the reverse complement. 
#Print to STDOUT and capture the output into a file with a command line redirect '>'.

#Previously we were able to generate reverse complements with the following code:
#dna_comp  = dna12.upper().replace('A','t').replace('T','a').replace('C','g').replace('G','c')
#dna12_rev = dna_comp[::-1]
#print(f'The reverse complement of {dna12} is {dna12_rev.upper()}.')

gene7 = {}
with open("Python_06.seq.txt","r") as Q7R, open("Python_07.fa","w") as Q7W:
    for line in Q7R:
        #split based on the tab deliminator
        line = line.rstrip() #remove the \n from the end of each line
        gene_id,seq = line.split('\t') #split on \t
        gene7[gene_id] = seq
        #Generate the reverse compliment of the line
        seq = line.upper() #Uppercase each line to ensure uniformity of input
        seq = seq.replace('A','t').replace('T','a').replace('C','g').replace('G','c') #complement seq
        seq = seq[::-1] #reverse it
        gene7[gene_id] = seq #update the dictionary to include key: gene | variable = reverse complement seq
    for gene in gene7: #write from the dictionary
        seq_rc = gene7[gene]
        Q7W.write(f'>{gene:<10}: This is the reverse complement. \t {seq_rc} \n')

#./Py3Set6Q1.py > Python_07.fa <-- to write STDOUT to file instead of the last bit!
# gene7 = {}
# with open("Python_06.seq.txt","r") as Q7R, open("Python_07.fa","w") as Q7W:
#     for line in Q7R:
#         #split based on the tab deliminator
#         line = line.rstrip() #remove the \n from the end of each line
#         gene_id,seq = line.split('\t') #split on \t
#         gene7[gene_id] = seq
#         #Generate the reverse compliment of the line
#         seq = line.upper() #Uppercase each line to ensure uniformity of input
#         seq = seq.replace('A','t').replace('T','a').replace('C','g').replace('G','c') #complement seq
#         seq = seq[::-1] #reverse it
#         gene7[gene_id] = seq #update the dictionary to include key: gene | variable = reverse complement seq
#     for gene in gene7: #write from the dictionary
#         seq_rc = gene7[gene]
#         print(f'>{gene:<10}: This is the reverse complement. \t {seq_rc} \n')

##Question 8: Open the FASTQ file Python_06.fastq and go through each line of the file.
#Count the number of lines and the number of characters per line. Have your program report the average line length

line_sum = 0
char_sum = 0
with open("Python_06.fastq.f","r") as Q8R:
    for line in Q8R:
        #split based on the tab deliminator
        line = line.rstrip() #remove the \n from the end of each line
        #print(len(line)) #the number of characters per line
        line_sum += 1
        char_sum += len(line)
#Calculate average line length
    print(f'The line total is: {line_sum}') #print the total lines
    print(f'The character total is: {char_sum}')
    print(f'The average line length is {char_sum/line_sum}') #print #the average line length

##Question 9: Write your first FASTA parser script. This is a script that reads in a FASTA file 
# and stores each FASTA record separately for easy access for future analysis.
# Things to keep in mind:

    #open your file
    #read each line
    #is your line a header line? is it a sequence line?
    #does a single FASTA record have one line of sequence or multiple lines of sequence?

gene9 ={}
gene_hd = 'x'
with open("Python_06.fasta","r") as Q9R:
    for line in Q9R:
        #split based on the tab deliminator
        line = line.rstrip() #remove the \n from the end of each line
        #If it has > it's a header
        if line.startswith(">"):
        #if line.find(">"): THIS WAS ALWAYS TRUE, WHEN NOT FOUND
        #-1 IS STILL TRUE.
            gene_hd = line
            gene9[line] = ''
            
        else:
            gene9[gene_hd] += line #+= to append! Not Overwrite!
print(f'fastaDict = {gene9}')        
        
##Question 10: Goal of this problem: generate a couple of gene
# list that are saved in files, add their contents to sets, and compare them.       

#Open each of the three files and add the geneIDs (Gene stable ID) to a Set. One Set per file.

all_set = set()
stm_set = set()
pig_set = set()

with open("ferret_all_genes.tsv","r") as RS101:
    for line in RS101:
        line = line.rstrip() #remove the \n from the end of each line
        all_set.add(line)
with open("ferret_stemcellproliferation_genes.tsv","r") as RS102:
    for line in RS102:
        line = line.rstrip() #remove the \n from the end of each line
        stm_set.add(line)
with open("ferret_pigmentation_genes.tsv","r") as RS103:
    for line in RS103:
        line = line.rstrip() #remove the \n from the end of each line
        pig_set.add(line)

#A. Find all the genes that are not cell proliferation genes.

all_set.remove('Gene stable ID')
stm_set.remove('Gene stable ID')
pig_set.remove('Gene stable ID')

#print(all_set)

print(f'The genes that are not stem cell proliferation genes include: {all_set - stm_set}')

#B. Find all genes that are both stem cell proliferation genes and pigment genes.
#Note Make sure to NOT add the header to your set.

print(f'The genes that are both stem cell proliferation genes and pigment genes are: {pig_set | stm_set}')

tf_set = set()
with open("ferret_transcriptionFactors.tsv","r") as RS104:
    for line in RS104:
        line = line.rstrip() #remove the \n from the end of each line
        tf_set.add(line)
tf_set.remove('Gene stable ID')

print(f'The genes that are both stem cell proliferation genes and transcription factor genes are: {tf_set & stm_set}')
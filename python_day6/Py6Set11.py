#!/usr/bin/env python3

###Python Problem Set 11: Classes



#Q1: Create a DNA sequence class that will contain a sequence, its name, and it's organism of origin.
# Do this by creating an __init__ function.

class DNASeq(object):
    #Define Class Attributes
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name

#Q2: Write some some lines of code, outside your class (in your main program) that sets the name,
# DNA sequence, and organism for a gene.

dna = 'TAATTAAT'
gene = 'Box'
species = 'Peeps'

#Q3: Write some some lines of code, outside your class that:
#     a. uses the object sequence attribute to retrieve and print the sequence.
#     b. uses the object name attribute to retrieve and print the name.
#     c. uses the object organism attribute to retrieve and print the organism.

print(f'Print Sequence Attribute: {dna}')
print(f'Print Gene Name Attribute: {gene}')
print(f'Print Organism Attribute: {species}')

#Q4: Sequence length method
#     a. Add a method to your class that caclulates and returns the length of the sequence.
#     b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence length using your new method.

class DNASeq(object):
    #Define Class Attributes
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
    #Define Class Methods
    def seqsize(self):
        length = len(self.sequence)
        return length

dummydna = DNASeq('TAATTAAT','Box','Peeps')


print(f"Print DNASeq Object {dummydna.gene_name}'s sequence: {dummydna.sequence}")
print(f"Print length of sequence for {dummydna.gene_name}: {dummydna.seqsize()}")

#Q5: Nucleotide composition method
#     a. Add in a method that caclulates and returns the nucleotide composition.
#     b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence nucleotide compositio using your new method.

class DNASeq(object):
    #Define Class Attributes
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
    #Define Class Methods
    def seqsize(self):
        length = len(self.sequence)
        return length
    def percentGC(self):
        c_count = self.sequence.count('C')
        g_count = self.sequence.count('G')
        dna_len = len(self.sequence)
        gc_content = (c_count + g_count)/dna_len
        return gc_content
    def nuccomp(self):
        nt_comp ={'A':0,'T':0,'G':0,'C':0}
        nt_comp['A'] = self.sequence.count('A')
        nt_comp['T'] = self.sequence.count('T')
        nt_comp['G'] = self.sequence.count('G')
        nt_comp['C'] = self.sequence.count('C')
        return nt_comp

dummydna = DNASeq('TAATTAAT','Box','Peeps')
print(f"Print the nucleotide composition for {dummydna.gene_name}: {dummydna.nuccomp()}")

#Q6: GC content method
#     a. Add in a method that caclulates and returns the GC content.
#     b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence GC content using your new method.

class DNASeq(object):
    #Define Class Attributes
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
    #Define Class Methods
    def seqsize(self):
        length = len(self.sequence)
        return length
    def percentGC(self):
        c_count = self.sequence.count('C')
        g_count = self.sequence.count('G')
        dna_len = len(self.sequence)
        gc_content = (c_count + g_count)/dna_len
        return gc_content

dummydna = DNASeq('TAATTAAT','Box','Peeps')
Gummydna = DNASeq('GGGGGGGG','Bear','Peeps')

print(f"Print DNASeq Object {Gummydna.gene_name}'s sequence: {Gummydna.sequence}")
print(f"Print GC of sequence for {Gummydna.gene_name}: {Gummydna.percentGC():.1%}")
print(f"Print DNASeq Object {dummydna.gene_name}'s sequence: {dummydna.sequence}")
print(f"Print GC of sequence for {dummydna.gene_name}: {dummydna.percentGC():.1%}")

#Q7: FASTA Formatter method
#     a. Add in a method that returns the sequence record in FASTA format.
#     b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence in FASTA format using your new method.

class DNASeq(object):
    #Define Class Attributes
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
    #Define Class Methods
    def seqsize(self):
        length = len(self.sequence)
        return length
    def percentGC(self):
        c_count = self.sequence.count('C')
        g_count = self.sequence.count('G')
        dna_len = len(self.sequence)
        gc_content = (c_count + g_count)/dna_len
        return gc_content
    def nuccomp(self):
        nt_comp ={'A':0,'T':0,'G':0,'C':0}
        nt_comp['A'] = self.sequence.count('A')
        nt_comp['T'] = self.sequence.count('T')
        nt_comp['G'] = self.sequence.count('G')
        nt_comp['C'] = self.sequence.count('C')
        return nt_comp
    def FastaFormater(self, char='\n'):
        import re #YOU CAN IMPORT MODULES WITHIN A FUNCTION!
        no_new_lines = self.sequence.replace("\n","")
        fastaseq60 = char.join(no_new_lines[i:i+60] for i in range(0, len(no_new_lines), 60))
        return(f'>{self.gene_name}:\n{fastaseq60}')

Gummydna = DNASeq('GGGGGGGG','Bear','Peeps')
print(f"Print FastaFormat for {Gummydna.gene_name}:\n{Gummydna.FastaFormater()}")
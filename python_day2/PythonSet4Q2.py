#!/usr/bin/env python3

#Python Problem Set 4 - Question 2:


import sys

taxa_string = 'sapiens : erectus : neanderthalensis'

#B:

print(f'{type(taxa_string)}:{taxa_string}')
print(f'string: {taxa_string}')

#C:
taxa_list = taxa_string.split(' : ')

#D:
print(taxa_list)

#E:
print(taxa_list[1])
#You get erectus.

#F:
print(type(taxa_string)
#You get class 'str'.
print(type(taxa_list))
#You get <class 'list'>.

#G:
alp_list = sorted(taxa_list, key=str.lower, reverse=False)
#['erectus', 'neanderthalensis', 'sapiens']

#H:Sort the list by length of each string and print, shortest to longest.

sorted_taxa_list = sorted(alp_list, key = len)
print(sorted_taxa_list)
#['sapiens', 'erectus', 'neanderthalensis']


















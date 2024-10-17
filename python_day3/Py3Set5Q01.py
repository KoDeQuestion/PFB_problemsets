#!/usr/bin/env python3

###Python Problem Set 5

##Question 1:

#Construct a dictionary of your favorite things:

fav_dic = {'game':'League of Legends','drink':'Campari', 'tree':'Birch', 
'book':'Diamond Age', 'song': 'Illenium - Lost'}

#print(fav_dic)

##Question 2: Print out your favorite book.

print(fav_dic['book'])

##Question 3: Print out your favorite book but use a variable in the key.

fav_thing = 'book'
print(f'My favorite {fav_thing} is {fav_dic[fav_thing]}')

fav_thing = 'game'
print(f'My favorite {fav_thing} is {fav_dic[fav_thing]}')

##Question 4: Now print your favorite tree.

fav_thing = 'tree'
print(f'My favorite {fav_thing} is {fav_dic[fav_thing]}')

##Question 5: Add your favorite 'organism' to the dictionary. Make organism the new key of fav_thing.

fav_dic['organism'] = 'Human'
print(fav_dic)

fav_thing = 'organism'
print(fav_dic[fav_thing])

##Question 6: Use a for loop to print out each key and value of the dictionary.

for thing in fav_dic:
    print(f'{thing:10} \t {fav_dic[thing]}')

##Questions 7: Take a value from the command line for fav_thing and print the value of that item from the dictionary.

import sys

#fav_thing = sys.argv[1]
#print(fav_dic[fav_thing])

# fav_thing = sys.argv[1] if len(sys.argv) > 1 else None
# if fav_thing
#     print(fav_dic[fav_thing])
# else:
#     continue

##Question 8: Print out all the keys to the user so that they know what to pick from. Check out input(). 

ask = input(f'Type one {list(fav_dic.keys())} for the favorite:')
print('It is ' + fav_dic[ask])
#ask = input(f'Enter a {fav_dic.keys()} you favorite:')
#print('It is ' + fav_dic[ask])

##Question 9: Change the value of your favorite organism.

fav_dic['organism'] = 'Cat'

##Question 10: Get the fav_thing from the command line and a new value for that key. Change the value with the user inputted value. And print out a confirmation.

ask2 = input(f'Type one {list(fav_dic.keys())} for the favorite:')
ask3 = input(f'Type your favorite {ask2}:')

fav_dic[ask2] = ask3

for thing in fav_dic:
    print(f'{thing:10} \t {fav_dic[thing]}')
print('\n')
##Extra:
capitalized_dic = {key.capitalize(): value for key, value in fav_dic.items()}
for thing in capitalized_dic:
    print(f'{thing:10} \t {capitalized_dic[thing]}')

#from char_classes import * #What is char_classes?
from character_class import *
import pickle

#
#   Info gotten is:
#       1: Name
#       2: Race
#       3: Class
#       4: Stats
#
#########################################################
#
#   Made attributes and stats into dictionaries.
#   attribute keys are now : 'name', 'race', 'class'
#   stats keys are now: 'stats' and 'mods'
#

heading = '====================================='
print(heading)
print('========== Start Character ==========')
print(heading)
print('>>')
'''
char_name = str(input('>> First things first, Character Name: '))
print('>>')
print('>> Duuuuuude. Sick name, duuude.')
print('>>')
'''
print('>> So, brah, do you want to make or load a char, bruh?')

while True:
    print('>> load -- new')
    load_check = str(input('>> '))

    if load_check == 'new':
        print('\n'+heading+'\n\n'+heading+'\n>>')
        char_name = str(input('>> First things first, Character Name: '))
        print('>>')
        print('>> Duuuuuude. Sick name, duuude.')
        print('>>')
        run = Character(char_name, False)

    elif load_check == 'load':
        print('>> Sick, brah. What\'s your bud\'s name?')
        now = str(input('>> '))

        try:
            run = Character(now, True) #loading the charater from pcikel.
            break

        except FileNotFoundError:
            print(now)
            print('>> Uh oh spaghetti bro\'s')
            print(">> Looks like that isn't a character yet...")
            print(">> (or maybe it's a ghost bro hahah)")
            print('\n'+heading)
            print(heading+'\n')

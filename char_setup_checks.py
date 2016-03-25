from race_class_loader import *
from character_class import *

#
#   Something is wrong with the level thing. It prints the level taker after every skill
#
#   Changed the loop checker to get a race from the list to a 'if char_race in...' thing.
#

def race(): #Check's if the user has chosen an actual race.
    #races = ['Elf', 'Human', 'Half-Elf', 'Half elf', 'Half Elf', 'Half Orc','Dwarf', 'Halfling', 'Dragonborn', 'Teifling']
    race_keys = {'Dwarf':'dw','Elf':'el', 'Halfling':'hl', 'Half-Elf':'he','Half-Orc':'ho', 'Dragonborn':'db', 'Human':'hu', 'Teifling':'tl'}
    while True:
        _carriage = []
        print('>> The races be: ')
        print('-- Dwarf | Elf | Halfling --')
        print('-- Half-Elf | Half-Orc | Human --')
        print('-- Dragonborn | Teifling --')
        char_race = str(input('>> Choose a race, dude: '))
        if char_race in race_keys:
            print('>> Duuuuude, I love', char_race+'s, brah.')
            fin_race = race_keys[char_race]
            return fin_race
        else:
            print('>> Whu? is that a race?')



def c_class():
    class_keys = {'Barbarian':'bb', 'Bard':'bd', 'Cleric':'cl', 'Druid':'dr', 'Monk':'mo', 'Fighter':'fi', 'Paladin':'pa', 'Ranger':'ra', 'Rogue':'ro','Sorcerer':'so','Warlock':'wa','Wizard':'wz'}
    while True:
        _carriage = []
        print('>> The classes are: ')
        print('-- Barbarian | Bard --')
        print('-- Cleric | Druid | Monk --')
        print('-- Fighter | Paladin --')
        print('-- Ranger | Rogue | Sorcerer --')
        print('-- Warlock | Wizard --')
        char_class = str(input('>> Choose a Class, brah: '))
        if char_class in class_keys:
            return class_keys[char_class]
        else:
            print('>> Wh- what, bro. Is that... is that a class?')



def stat_check(stat_type):
    while True:
        try:
            stat = int(input(stat_type))
            if stat > 30:
                print('>> Dude, stats only go to, like... 30, bro.')
            elif stat <=3:
                print('>> Stats usually only go down to three, so...')
            else:
                return stat
        except ValueError:
            print('>> Wha? That... isn\'t a number, man.')
        print('>> Try agian I guess?')



def level_check():
    while True:
        level = int(input('>> What level you starting at, braaaaaah: '))
        if level > 0 and level <31:
            return level
        else:
            print('>> Oops, dude. Levels are only between 1 and 30 brah.')



def stat_mod(stat):
    print('>> What level you starting at, braaaaaah: ')
    if stat >= 10:
        mod = int((stat - 10) / 2)
    elif stat < 10:
        mod = int((abs(stat-11)/2)*-1)
    return mod



def setup():
    heading = '====================================='
    """
    print(heading)
    print('===========Start Character===========')
    print(heading)
    print('')
    char_name = str(input('>> First things first, Character Name: '))
    """

    char_race = race()
    print('>>')
    char_class = c_class()
    print('>>')

    print('>> Braaaaaah. Wiiiickeeeeed.')
    print('>>')
    char_level = level_check()
    char_eyes = str(input('>> What\'s your eye color duude: '))
    print('>> Hahahha pretty sick, duuuuude.')
    print(heading)
    print('\n')
    print(heading)

    ### Now the Stats

    print('=== Now the totally rad part brah ===')
    print('=============== STATS ===============')

    STR = stat_check('>> Put your strength stat, brah: ')
    STR_mod = stat_mod(STR)
    print('>> Radical, man. Your strenght mod is', STR_mod, 'btdubs.')

    DEX = stat_check('>> Dex Time dude: ')
    DEX_mod = stat_mod(DEX)
    print('>> Sweeeeet.', str(DEX_mod),'ain\'t bad, bro')

    CON = stat_check('>> Con (it\'s important too): ')
    print('>> Broooo. You\'re tough as balls, broo.')

    WIS = stat_check('>> Wissy wissard hahaha: ')

    INT = stat_check('>> Int is for nerds: ')

    CHA = stat_check('>> Cha-Ching Charismo bro: ')
    print('>> Time to pick up the babes am I right brah hahaha.')
    print('>> Or bros, man, what ever you is brah haha.')


    char_attributes = {'race':char_race,'class':char_class}
    char_stats = {'str':STR,'dex':DEX,'con':CON,'wis':WIS,'int':INT,'cha':CHA}
    return char_attributes, char_level, char_stats

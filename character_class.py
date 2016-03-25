from char_setup_checks import *
from race_class_loader import *
from items import *
import pickle

#
#   1: Make class  // Tick-ish
#   2: Make the class take the info from setup // Tick
#   3: Take info from race_class document and put it into the Character //
#   4: pickle info into somewhere. // Tick
#   5: make a weapon class
#   6: get class profs into skills_with_prof
#   7:
#
#   Because 'class' gets confused with (def) class I made everything caps.
#
#   'Don't even trip, dog'-- Rick Sanchez
#

class Character(object):

    """
        Taking the information from setup and saving it
        I guess it's just important to remember caps.

        the load parameter on __init__ is either True
        or False depending if the character has already
        been setup.
    """

    def __init__(self, name, load):
        if load == False:
            self.new_setup(name)
            self.constants(name)

        elif load == True:
            self.load_setup(name)

        self.menu()

    def constants(self, name):
        self.name = name
        self.str = self.sts['str']
        self.dex = self.sts['dex']
        self.con = self.sts['con']
        self.int = self.sts['int']
        self.wis = self.sts['wis']
        self.cha = self.sts['cha']
        self.prof_boni = [None, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]
        self.skill_setup()


    def load_setup(self, name):
        payload = pickle.load(open(str(name)+'_save.p', "rb"))
        self.attributes = payload[0]
        self.level = payload[1]
        self.sts = payload[2]
        self.RACE = payload[3]
        self.CLASS = payload[4]
        self.skills_with_prof = payload[5]


    def new_setup(self, name):
        races = pickle.load(open('races.p', 'rb'))
        classes = pickle.load(open('classes.p', 'rb'))
        self.attributes, self.level, self.sts = setup()
        self.RACE = races[self.attributes['race']]
        self.CLASS = classes[self.attributes['class']]
        print('-- Hey, dude, you get to choose', self.CLASS['profs']['skills'][0],'skillllzz ')
        print('-- to be proficient with out of this conviniently placed list')
        self.skills_with_prof = []
        self.skill_prof_chooser()

        #pickle.dump(self, char_saves.py,*,fix_imports=True)

    def menu(self):
        _help = "--- Options: ---\n>> stats / skill <<\n>> help / quit <<\n>> attack / save <<\n>>"
        print(_help)
        self.options = {
        'save':self.save,
        'skill':self.my_skills,
        'stats':self.my_stats,
        'stat':self.my_stats,
        'save':self.save
        }
        while True:
            key = str(input('>> '))
            key = key.lower()
            if key in self.options:
                self.options[key]()
            elif key == 'quit':
                print('--------------------------')
                print('>> You wanna save first, dude?')
                _save_ask = str(input('>> (y / n): '))
                if _save_ask.lower() == 'y':
                    self.save()
                print('>> Catcha later, duuude.')
                break
            elif key == 'help':
                print(_help)

    def skill_prof_chooser(self):
        print(self.CLASS['profs']['skills'][1:])
        skills_to_choose = self.CLASS['profs']['skills'][0]
        while skills_to_choose > 0:
            chosen_skill = str(input('>> '))
            self.skills_with_prof.append(chosen_skill)
            skills_to_choose -= 1

    def skill_setup(self):
        self.str_skills = [self.stat_mod(self.str),{'Athletics': False}]
        self.dex_skills = [self.stat_mod(self.dex),{'Acrobatics':False, 'Slight of Hand':False, 'Stealth':False}]
        self.int_skills = [self.stat_mod(self.int),{'Perception':False, 'Arcana':False, 'History':False, 'Investigation':False, 'Nature':False, 'Religion':False}]
        self.wis_skills = [self.stat_mod(self.wis),{'Insight':False, 'Animal Handling':False, 'Medicine':False, 'Perception':False, 'Survival':False}]
        self.cha_skills = [self.stat_mod(self.cha),{'Deception':False, 'Intimidation':False, 'Performance':False, 'Persuasion':False}]
        self.skills = [self.str_skills, self.dex_skills, self.int_skills, self.wis_skills, self.cha_skills]
        for lst in self.skills:
            for thing in self.skills_with_prof:
                item = thing.capitalize()
                if item in lst[1]:
                    lst[1][item] = True
                    print('>>', lst[1])
                    print('>>',lst[1][item],'is now true')

    def my_skills(self):
        '''
            So this goes through the self.skills one list at a time:
                if the input is in the
        '''
        curr_list = 0
        print('>> Which skill ya need bruh.')
        case_skill = str(input('>> '))
        skill = case_skill.capitalize()
        mod = 0
        for lst in self.skills:
            if skill in lst[1]:
                mod += lst[0]
                if lst[1][skill] == True:
                    print('-- You got prooffffzzz')
                    print(self.prof_boni[self.level])
                    mod += self.prof_boni[self.level]
                else:
                    print("-- ya Dont got prooffffzzz")
            else:
                curr_list += 1
        print(mod)

    def my_items(self):
        """This is a place holder at the moment until I get
        Actuall items up in theis beithc"""
        items = self.str

    def my_

    def my_race(self):
        race_print = str(input('>> What you need, bro: '))
        try:
            print('-- Ok, bro, your',race_print,'be',self.RACE[race_print])

        except KeyError:
            print('-- Wh- what.')

    def my_stats(self):
        stat_print = str(input('>> What stat you need, bro?\n>> [str - con - dex - wis - int - cha]\n>> '))
        try:
            print('-- Your',stat_print,'is', self.sts[stat_print],'--')
            print('-- And your',stat_print,'modifier is',self.stat_mod(self.sts[stat_print]),'--')

        except KeyError:
            print('-- Uh, what.')
            print('-- You can type str, con, dex, wis, int, or cha.')
            print("-- Or you can type 'quit' to quit, dog.")


    def attack(self):
        wep = str(input('-- What are you attacken with, bruh: '))

    def stat_mod(self, stat):
        if stat >= 10:
            mod = int((stat - 10) / 2)

        elif stat < 10:
            mod = int((abs(stat-11)/2)*-1)

        return mod

    def save(self):
        payload = [self.attributes, self.level, self.sts, self.RACE, self.CLASS, self.skills_with_prof]
        pickle.dump(payload, open(str(self.name)+'_save.p', "wb"))
        print('-- radical brah,', self.name, 'got saved 8)')

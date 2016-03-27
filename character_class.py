from char_setup_checks import *
#from race_class_loader import *
import pickle

#
#   1: Make class  // Tick-ish
#   2: Make the class take the info from setup // Tick
#   3: Take info from race_class document and put it into the Character //
#   4: pickle info into somewhere. // Tick
#   5: make a weapon class
#   6: get class profs into my_profs
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
        self.spaghetti = '-- Uh oh, Spaghetti O\'s, brooohh'
        self.str = self.sts['str']
        self.dex = self.sts['dex']
        self.con = self.sts['con']
        self.int = self.sts['int']
        self.wis = self.sts['wis']
        self.cha = self.sts['cha']
        print('-- HP time, bro. \n-- Roll',self.level,'d',str(self.CLASS['hit_di'][1]),'dawg.')
        self.HP = int(input('>> '))
        self.prof_boni = [None, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]
        self.skill_setup()


    def load_setup(self, name):
        payload = pickle.load(open(str(name)+'_save.p', "rb"))
        self.attributes = payload[0]
        self.level = payload[1]
        self.sts = payload[2]
        self.RACE = payload[3]
        self.CLASS = payload[4]
        self.my_profs = payload[5]
        self.HP = payload[6]
        self.skills = payload[7]


    def new_setup(self, name):
        races = pickle.load(open('races.p', 'rb'))
        classes = pickle.load(open('classes.p', 'rb'))
        self.attributes, self.level, self.sts = setup()
        self.RACE = races[self.attributes['race']]
        self.CLASS = classes[self.attributes['class']]
        print('-- Hey, dude, you get to choose', self.CLASS['profs']['skills'][0],'skillllzz ')
        print('-- to be proficient with out of this conviniently placed list')
        self.my_profs = {}
        self.prof_chooser()

        #pickle.dump(self, char_saves.py,*,fix_imports=True)

    def menu(self):
        _help = "--- Options: ---\n-- stats / skill --\n-- help / quit --\n-- attack / save --\n-- deets --\n"
        print(_help)
        self.options = {
        'save':self.save,
        'skill':self.my_skills,
        'stats':self.my_stats,
        'stat':self.my_stats,
        'save':self.save,
        'deets':self.my_deets,
        'attack':self.attack
        }
        while True:
            key = str(input('>> '))
            key = key.lower()

            if key in self.options:
                self.options[key]()

            elif key == 'quit':
                print('--------------------------')
                print('-- You wanna save first, dude?')
                _save_ask = str(input('>> (y / n): '))
                if _save_ask.lower() == 'y':
                    self.save()
                print('-- Catcha later, duuude.')
                break

            elif key == 'help':
                print(_help)

            else:
                print('-- oh, dude, uh, I dont think I got that.')

    def prof_chooser(self):
        '''
            this is where the player decides the profs from CLASS and RACE.
                Tools,
                skills,
                armour,
                weapons,

        '''
        def chooser(num_choices, list_choices, type_choice):
            '''
            num_choices is how many things the player can choose (index 0 on list)
            list_choices is a list what the player can choose from (index 1: on list)
            type_choice is string of what key the prof goes under (skill, tool, armour, etc)
            '''
            while int(num_choices) > 0:
                print('--',list_choices)
                chosen = str(input('>> '))

                if chosen in list_choices:
                    self.my_profs[type_choice].append(chosen)
                    list_choices.remove(chosen)
                    num_choices -= 1

                else:
                    print(self.spaghetti)
                    print('-- looks like that aint on the list haha')

        self.my_profs['skills'] = []
        list_skills = self.CLASS['profs']['skills'][1:]
        num_skills = self.CLASS['profs']['skills'][0]
        chooser(num_skills,list_skills,'skills')

        self.my_profs['tools'] = []
        list_tools = self.RACE['profs']['tools'][1:]
        num_tools = self.RACE['profs']['tools'][0]
        chooser(num_tools,list_tools,'tools')
        """
        ### Skills ###

        while num_skills > 0:
            print('--',list_skills)
            chosen_skill = str(input('>> '))

            if chosen_skill in list_skills:
                self.my_profs['skills'].append(chosen_skill)
                list_skills.remove(chosen_skill)
                num_skills -= 1

            else:
                print("-- Looks like that ain't on the list.")
                print('--')


        ### Tools ###
        if 'tools' in self.RACE['profs']:
            self.my_profs['tools'] = []
            num_tools = self.RACE['profs']['tools'][0]
            list_tools = self.RACE['profs']['tools'][1:]

            while num_tools > 0:
                print(list_tools)
                chosen_tool = str(input('>> '))

                if chosen_tool in list_tools:
                    self.my_profs['tools'].append(chosen_tool)
                    list_tools -= chosen_tool
                    num_tools -= 1

                else:
                    print('-- Uh oh spaghetti o\'s brah hahha')

        if 'weps' in self.RACE['profs']:
            if self.RACE['profs']
        """

    def skill_setup(self):
        self.str_skills = [self.stat_mod(self.str),{'Athletics': False}]
        self.dex_skills = [self.stat_mod(self.dex),{'Acrobatics':False, 'Slight of Hand':False, 'Stealth':False}]
        self.int_skills = [self.stat_mod(self.int),{'Perception':False, 'Arcana':False, 'History':False, 'Investigation':False, 'Nature':False, 'Religion':False}]
        self.wis_skills = [self.stat_mod(self.wis),{'Insight':False, 'Animal Handling':False, 'Medicine':False, 'Perception':False, 'Survival':False}]
        self.cha_skills = [self.stat_mod(self.cha),{'Deception':False, 'Intimidation':False, 'Performance':False, 'Persuasion':False}]
        self.skills = [self.str_skills, self.dex_skills, self.int_skills, self.wis_skills, self.cha_skills]

        for lst in self.skills:
            for thing in self.my_profs:
                item = thing.capitalize()

                if item in lst[1]:
                    lst[1][item] = True

    def my_skills(self):
        '''
            So this goes through the self.skills one list at a time:
                if the input is in the
        '''
        curr_list = 0
        print('-- Which skill ya need bruh.')
        case_skill = str(input('>> '))
        skill = case_skill.capitalize()
        mod = 0
        for lst in self.skills:

            if skill in lst[1]:
                mod += lst[0]

                if lst[1][skill] == True:
                    print('-- You got prooffffzzz')
                    mod += self.prof_boni[self.level]

                else:
                    print("-- ya dont got prooffffzzz")

            else:
                curr_list += 1

        print('-- you get to add', mod, 'to your role, bruh')

    def my_items(self):
        """This is a place holder at the moment until I get
        Actuall items up in theis beithc"""
        items = self.str

    def my_deets(self):
        print("-- All riiiiiiiiiightah")
        print("-- Let's check out some of your special deets, DAAWG")
        print('--------------------------')
        print('-- From your race we got:')
        print('---- Yo speed is',self.RACE['speed'], 'ft')
        print('---- Yo vision is', self.RACE['vision']['dim'], 'ft in dim light and',self.RACE['vision']['dark'], 'in dark lightin.')
        print('----', self.RACE['special'])
        print('---- Yo can fuck shit up with', ', '.join(self.RACE['profs']['weps']), '+ prooffffzzz broooooo thats pretty coool duude.')
        print('')

    def my_race(self):
        race_print = str(input('>> What you need, bro: '))

        try:
            print('-- Ok, bro, your',race_print,'be',self.RACE[race_print])

        except KeyError:
            print('-- Wh- what.')

    def level_up(self):
        self.level += 1

    def my_stats(self):
        stat_print = str(input('>> What stat you need, bro?\n>> [str - con - dex - wis - int - cha]\n>> '))

        try:
            print('-- Your',stat_print,'is', self.sts[stat_print],'--')
            print('-- And your',stat_print,'modifier is',self.stat_mod(self.sts[stat_print]),'--')

        except KeyError:
            print('-- Uh, what.')
            print('-- You can type str, con, dex, wis, int, or cha.')
            print("-- Or you can type 'quit' to quit, dog.")

    def my_tools(self):
        print('-- What tool ya need, bro')
        tool = str(input('>> '))
        print(tool)

    def attack(self):
        wep = str(input('-- What are you attacken with, bruh: '))

    def stat_mod(self, stat):
        if stat >= 10:
            mod = int((stat - 10) / 2)

        elif stat < 10:
            mod = int((abs(stat-11)/2)*-1)

        return mod

    def save(self):
        payload = [self.attributes, self.level, self.sts, self.RACE, self.CLASS, self.my_profs, self.HP, self.skills]
        pickle.dump(payload, open(str(self.name)+'_save.p', "wb"))
        print('-- radical brah,', self.name, 'got saved 8)')

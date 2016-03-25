import pickle
#
#   This loads the data from the D&D class into the class class. Yeah
#
#       Woohoo indents
#
#   Yo dog. Keep it real.
#
#   Added 'Size' dictionaries for M or S.
#   Resistances works like:
#       Key: What you have resistance against
#       Data: Either True of False.
#
#   Skill proficiencies work by:
#       Val1 = how many you can have (like, choose two)
#       Val2: = choices
#
#   Index of proficiency boni:
#       None is the first value so the indeces line up with the levels
#
#
#   Not sure how to put 'Dwarves have Advantage against Poison.'
#   Add saving throws later
#

foo = 'bar'

Dwarf       = {'abil_increase':{'CON':2},
               'speed':25,
               'vision':{'dim':60,'dark':'bw'}, #bw means black and white only
               'special':You are proficient with History if you\'re checking the origin of a cut stone.',
               'profs':{
                    'weps':{'battleaxe':True,'handaxe':True,'throwing hammer':True, 'warhammer':True},
                    'tools':[1, 'smith','brewer','mason'] # slice it so that ['tools'][0] comes up as the amount of tools you can be proficient with and ['tools'][1:] are the choices
                    },
               'res':'poison', #Resistances from types of damage
               'langs':['Common', 'Dwarvish'],
               'sub_race':[foo]
               }

High_Elf    = {'abil_increase':{'INT':1}}

Wood_Elf    = {'foo':foo}

Drow        = {'foo':foo}

Elf         = {'abil_increase':[foo],
               'speed':25,
               'vision':[foo],
               'special':{'Trance':'Ye'},
               'profs':['Perception'],
               'langs':[foo],
               'sub_race':[High_Elf,Wood_Elf,Drow,]
               }

Halfling    = {'abil_increase':[foo],
               'speed':25,
               'vision':[foo],
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Human       = {'abil_increase':[foo],
               'speed':25,
               'vision':[foo],
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Dragonborn  = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Gnome       = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Half_Elf    = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Half_Orc    = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Teifling    = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }


#-------------------------------------------------------------------------------------#



q, t = 1, 2
lvl_1 = 'le'
higher = 'er'
armour = 'thing'
weapons = ' I eat memory ' #these are here just to not throw errors.
tools = 23432              # I'll put the rest of the pirated stats in later.
skills = 'money'           # 'Cool beans, dog' -- dubPirate
Barbarian = {
             'features':[],
             'cantrips':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Bard      = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Cleric    = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Druid     = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Monk       = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Fighter    = {'features':[None, {'Fighting Style':'Description', 'Second Wind':'Description'}],
             'cantrips':['bangles'],
             'spell_slots':[None],
             'hit_di':[1,10], #q is for quantity; t is for type
             'hit_points':['10 + CON,hit_di + self.CON'],
             'profs':{ 'armour':'all', 'weapons':['simple', 'martial'], 'tools':None, 'skills': [2, 'acrobatics', 'animal handling', 'athletics', 'history', 'insight', 'intimidation','perception','survival'] }
             }

Paladin   = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Ranger    = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Rogue     = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Sorcerer  = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Warlock   = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Wizard    = {
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

"""
    The Races dict keys:
            dw = Dwarf
            el = Elf
            hl = Halfling
            he = Half-Elf
            ho = Half-Orc
            db = Dragonborn
            hu = Human
            tl = Teifling

    The Classes dict keys:
            bb = Barbarian
            bd = Bard
            cl = Cleric
            dr = Druid
            mo = Monk
            fi = Fighter
            pa = Paladin
            ra = Ranger
            ro = Rogue
            so = Sourcerer
            wa = Warlock
            wz = Wizard
"""

the_races = {'dw':Dwarf,'el':Elf,'hl':Halfling,'he':Half_Elf,'ho':Half_Orc,'db':Dragonborn, 'hu':Human, 'tl':Teifling}
the_classes = {'bb':Barbarian, 'bd':Bard, 'cl':Cleric, 'dr':Druid, 'mo':Monk, 'fi': Fighter, 'pa': Paladin, 'ra': Ranger, 'ro':Rogue,'so':Sorcerer,'wa':Warlock,'wz':Wizard}

pickle.dump(the_races, open('races.p',"wb" ))
pickle.dump(the_classes, open('classes.p', "wb"))
#-------------------------------------------------------------------------------------#

''' The Following is redundant '''
#class Race:
#    """Love peebs""" #What are peebs?
#    '''I'm going to use this to load classes into a class and then load that into the character class.'''
#    def __init__(self, race):
#        self.

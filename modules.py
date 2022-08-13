import random
from generateplayers import *


# The Map
# 1 2 3
# 4 5 6
# 7 8 9

def prompt():
    while True:
        command = input('> ')
        print('ECHO', command)
        if command.lower() == 'quit':
            break


def helloworld():
    print('Hello World!')


class Homosapien:
    def __init__(self, first, last, health):
        self.first = first
        self.last = last
        self.health = health

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Path Default String
path = 'You take the path to the '

# Paths
roompaths = [
    'a path to the south and east.',
    'a path to the west, south, and east.',
    'a path to the west and south.',
    'a path to the north, east and south.',
    'a path to the north, east, south and west.',
    'a path to the north, south and west.',
    'a path to the north and east.',
    'a path to the west, north and east.',
    'a path to the west and north.',

]

# Commands / Misc Lists
commandlist = [
    'target',
    'walk away',
    'inspect area',
    'inspect people',
    'inspect corpses',
    'inspect animals',
    'inspect paths',
    'go to person',
    'attack target',
    '> ',
    'flee',
    'rest',
    'get up',
    'go',

]

fightCommandList = [
    'punch',
    'quit',
    '> ',
    'flee',
]

# String Numbers

stringNumbers = []
stringRange = 0

while stringRange != 100:
    stringRange += 1
    stringNumbers.append(str(stringRange))


def NotRecognized(variety):
    # Variety in error message
    not_reco_random = random.randint(1, variety)
    if not_reco_random == 1:
        print('** Command not recognized.')
    elif not_reco_random == 2:
        print('** That command does not exist.')
    elif not_reco_random == 3:
        print('** Invalid command.')
    else:
        print('** You should probably refer to the game instructions.')


def choiceNotReco(variety):
    not_reco_random = random.randint(1, variety)
    if not_reco_random == 1:
        print('** Enter a valid choice, or enter return.')
    elif not_reco_random == 2:
        print('** Choice not recognized.')

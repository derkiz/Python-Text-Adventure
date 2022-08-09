import random
from generateplayers import *


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


game_map = [1, 2, 3], [4, 5, 6], [7, 8, 9]

room_one_paths = 'a path to the south and east.'
room_two_paths = 'a path to the west, south, and east.'
room_three_paths = 'a path to the west and south.'
room_four_paths = 'a path to the north, east and south.'
room_five_paths = 'a path to the north, east, south and west.'
room_six_paths = 'a path to the north, south and west.'
room_seven_paths = 'a path to the north and east.'
room_eight_paths = 'a path to the west, north and east.'
room_nine_paths = 'a path to the west and north.'

# Commands / Misc Lists
commandlist = [
    'target',
    'walk away',
    'inspect area',
    'inspect people',
    'inspect animals',
    'inspect paths',
    'go to person',
    'attack target',
    '> ',
    'flee',
    'return',
    'rest',
    'get up',

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

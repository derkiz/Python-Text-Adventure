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

# Commands
commandlist = [
    'target',
    'walk away',
    'inspect area',
    'inspect people',
    'inspect animals',
    'inspect paths',
    'go to person',
    'attack target',

]


def Combat(player):
    pass

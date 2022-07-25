from modules import *
from generateplayers import *

location = ''

# Gameplay

# command = input('> ')
# if command.lower() != 'quit':

while True:
    # Spawn
    area = 'one'

    # Prompt
    command = input('> ')

    # Inspect Area
    if command.lower() == 'inspect area':
        print('You inspect the area.')
        print(f'You see {str(len(gen_list))} people. ')
        print(f'You see {room_one_paths}')

    # Inspect People
    if command.lower() == 'inspect people':
        print(f'You see {str(len(gen_list))} people. ')
        print(f'admin: {gen_list}')

    # Inspect Paths
    if command.lower() == 'inspect paths':
        print(f'You see {room_one_paths}')

    # Go to person
    if command.lower() == 'go to person':
        n = 0
        while n != len(gen_list):
            n += 1
            print(f'{n}: person {n}')

        goto = input('> ')
        int_goto = int(goto)
        if (int_goto - 1) in range(0, (len(gen_list))):
            print(f'You go to person {str(int_goto)}.')
            print(gen_list[int_goto - 1])

    # Inspect Animals

    # Quit
    if command.lower() == 'quit':
        print('You disconnect your player. You died.')
        break

from modules import *
from generateplayers import *

location = ''

# Gameplay

command = input('> ')
if command.lower() != 'quit':

    # Spawn
    location = 'one'

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
        print(goto)
        if int(goto) in range(1, (len(gen_list)+1)):
            print(f'You go to person {goto}.')
            print(gen_list[int(goto)])

    # Inspect Animals

else:
    print('quit')

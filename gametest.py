import random
from modules import *
from generateplayers import *

location = ''

# Gameplay Loop
while True:

    # Spawn
    area = 1

    # Target
    target = 0

    # Prompt
    command = input('> ')

    # Target
    if command.lower() == 'target':
        print(str(target))
        if target == 0:
            print('You have no target.')

     # Walk Away
    if command.lower() == 'walk away':
        print('You take a stroll.')
        target = 0

    # Inspect Area
    if command.lower() == 'inspect area':
        print('You inspect the area.')
        print(f'You see {str(len(gen_list))} people. ')
        print(f'You see {room_one_paths}')

    # Inspect People
    if command.lower() == 'inspect people':
        print(f'You see {str(len(gen_list))} people. ')
        print(f'admin: {gen_list}')

    # Inspect Animals

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
            target = (gen_list[int_goto - 1])

    # Attack

    # Say
    if (command.lower()[:5]) == '/say ':
        said_word = (command[5:])
        print(f'You said: {said_word}')

    # Quit
    if command.lower() == 'quit':
        print('You disconnected your player. You died.')
        break

    # If command is not recognized
    if (command.lower()[:5]) == '/say ':
        pass

    elif command.lower() not in commandlist:
        not_reco_random = random.randint(1, 4)
        if not_reco_random == 1:
            print('** Command not recognized.')
        elif not_reco_random == 2:
            print('** That command does not exist.')
        elif not_reco_random == 3:
            print('** Invalid command.')
        else:
            print('** You should probably refer to the game instructions.')

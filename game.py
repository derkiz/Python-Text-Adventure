import random
from modules import *
from generateplayers import *


# Spawn
area = 1

# Target
target = 0

# Gameplay Loop
while True:

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

    # Inspect Animals // To do //

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
            target = int(goto)
            print(f'You go to person {str(int_goto)}.')
            print(gen_list[int_goto - 1])
        else:
            print('Choice not recognized. Type a valid number.')

    # Attack // Incomplete //
    if command.lower() == 'attack target':
        if target == 0:
            print('You can not attack nothing.')
        elif target in range(1, len(gen_list)):
            Combat(gen_list[target])

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
        NotRecognized(4)

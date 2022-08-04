import random
from modules import *
from generateplayers import *

gen_list()

# Spawn
area = 1

# Target
target = 0

print(len(npc_list))

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
        print(f'You see {str(len(npc_list))} people. ')
        print(f'You see {room_one_paths}')

    # Inspect People
    if command.lower() == 'inspect people':
        print(f'You see {str(len(npc_list))} people. ')
        print(f'admin: {npc_list}')

    # Inspect Animals // To do //

    # Inspect Paths
    if command.lower() == 'inspect paths':
        print(f'You see {room_one_paths}')

    # Go to person
    if command.lower() == 'go to person':
        n = 0
        while n != len(npc_list):
            n += 1
            print(f'{n}: person {n}')

        while True:
            goto = input('> ')
            int_goto = int(goto)
            target = int(goto)

            if (int_goto - 1) in range(0, (len(npc_list))):
                print(f'You go to person {str(int_goto)}.')
                print(npc_list[int_goto - 1])
                break

            print('Choice not recognized. Type a valid number.')

    # Attack // Incomplete //
    if command.lower() == 'attack target':
        target = target - 1

        if target <= -1:
            print('You can not attack nothing.')

        elif target in range(0, len(npc_list)):
            print(f'You have entered combat with: {npc_list[target]}')

            while npc_list[target][1] > 0:
                command = input('> ')
                
                if command == 'flee':
                    print('You ran away.')
                    break

                if command == 'quit':
                    print('You can not quit in combat.')

                if command == 'punch':
                    print(f'You punched {npc_list[target]}.')
                    damage = random.randint(20, 30)
                    print(f'You dealt {str(damage)} damage.')
                    npc_list[target][1] - damage
                    print(f'{npc_list[target][0]} HP Remaining: {str(npc_list[target][1])}')

                if command.lower() not in fightCommandList:
                    NotRecognized(4)
            
            if npc_list[target][1] < 0:
                print(f'You killed {npc_list[target]}.')
            

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

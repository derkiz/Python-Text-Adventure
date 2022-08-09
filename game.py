import random
import time
from modules import *
from generateplayers import *

# Debugging

# print(target)
# print(npc_list)
# print(npc_health)

# Spawn
area = 1

# Target
target = 0
corpseTarget = 0

# Player HP
playerHP = 100

# Gameplay Loop
while True:

    # Prompt
    command = '> '
    command = input('> ')

    # Target
    if command.lower() == 'target':
        print(str(target))
        if target == 0:
            print('You have no target.')

     # Walk Away
    if command.lower() == 'walk away':

        if target == 0:
            print('You can not walk away from nothing.')

        else:
            print('You take a stroll.')

        target = 0

    # Rest
    if command.lower() == 'rest':
        print('You sit down and rest.')

        while playerHP != 100:

            playerHP += 25

            if playerHP == 100:
                time.sleep(2)
                print('You recover 25 HP. Current HP: 100.')

            if playerHP < 100:
                time.sleep(2)
                print(
                    f'You recover 25 HP. Current HP: {str(playerHP)}.'
                )

            if playerHP > 100:
                time.sleep(2)
                recovered = 100 - (playerHP - 25)
                print(
                    f'You recover {str(recovered)} HP. Current HP: 100.'
                )
                playerHP = 100

        time.sleep(1)
        print('You have replenished all of your HP. You get up.')

    # Inspect Area
    if command.lower() == 'inspect area':

        print('You inspect the area.')

        if len(npc_list) >= 2:
            print(f'You see {str(len(npc_list))} people.')
        elif len(npc_list) == 1:
            print('You see one person.')

        if len(npc_corpse) == 1:
            print('You see one dead person.')
        elif len(npc_corpse) >= 2:
            print(f'You see {len(npc_corpse)} dead people.')

        print(f'You see {room_one_paths}')

    # Inspect People
    if command.lower() == 'inspect people':

        if len(npc_list) >= 2:
            print(f'You see {str(len(npc_list))} people.')

        elif len(npc_list) == 1:
            print('You see one person.')

    # Inspect Corspes
    if command.lower() == 'inspect corpses':

        if len(npc_corpse) == 1:
            print('You see one corpse.')

        elif len(npc_corpse) >= 2:
            print(f'You see {len(npc_corpse)} corpses.')

        print(f'admin: {npc_list}')

    # Inspect Animals // To do //

    # Inspect Paths
    if command.lower() == 'inspect paths':
        print(f'You see {room_one_paths}')

    # Go to corpse
    if command.lower() == 'go to corpse':

        if len(npc_corpse) != 0:

            corpseCount = 0

            if len(npc_corpse) > 0:
                while corpseCount != len(npc_corpse):
                    corpseCount += 1
                    print(f'{corpseCount}: Corpse {corpseCount}')

                while True:
                    goto = input('> ')

                    if goto.lower() == 'return':
                        print('You cease your action.')

                    if goto in stringNumbers:

                        int_goto = int(goto)

                        if (int_goto - 1) in range(0, (len(npc_corpse))):
                            print(f'You go to corpse {str(int_goto)}.')
                            print(npc_corpse[int_goto - 1])
                            command = '> '
                            corpseTarget = int(goto)
                            target = 0
                            break

                    print('Choice not recognized. Enter a valid number.')

        else:
            print('There are no corpses to go to.')

    # Go to person
    if command.lower() == 'go to person':

        if len(npc_list) != 0:

            n = 0

            while n != len(npc_list):
                n += 1
                print(f'{n}: Person {n}')

            while True:
                goto = input('> ')

                if goto.lower() == 'return':
                    print('You cease your action.')
                    break

                if goto in stringNumbers:

                    int_goto = int(goto)

                    if (int_goto - 1) in range(0, (len(npc_list))):
                        print(f'You go to person {str(int_goto)}.')
                        print(npc_list[int_goto - 1])
                        command = '> '
                        target = int(goto)
                        corpseTarget = 0
                        break

                print('Choice not recognized. Enter a valid number.')

        else:
            print('There is no one to go to.')

    # Attack // Incomplete //
    if command.lower() == 'attack target':

        target = target - 1

        # print(target)
        # print(npc_list)
        # print(npc_health)

        if target <= -1:
            print('You can not attack nothing.')

        elif npc_health[target] <= 0:
            print('You can not attack dead players.')

        elif target in range(0, len(npc_list)):
            print(f'You have entered combat with: {npc_list[target]}')

            while npc_health[target] > 0:
                command = input('> ')

                if command.lower() == 'flee':
                    print('You ran away.')
                    command = '> '
                    target = 0
                    break

                if command.lower() == 'quit':
                    print('You can not quit in combat.')

                if command.lower() == 'punch':
                    print(f'You punched {npc_list[target]}.')
                    damage = random.randint(25, 45)
                    print(f'You dealt {str(damage)} damage.')
                    npc_health[target] -= damage

                    if npc_health[target] > 0:
                        print(
                            f'{npc_list[target]} has {str(npc_health[target])} HP remaining.'
                        )

                        # NPC Turn in Combat
                        time.sleep(1)
                        damage = random.randint(15, 40)
                        playerHP -= damage
                        print(
                            f'{npc_list[target]} punches you and deals {str(damage)} damage.')

                        if playerHP <= 0:
                            print('You died.')
                            command = 'wiheqw87wqzx54qw6e'
                            break

                        print(f'You have {str(playerHP)} remaing.')

                    if npc_health[target] <= 0:
                        print(f'You killed {npc_list[target]}.')
                        npc_corpse.append(npc_list[target])
                        npc_list.remove(npc_list[target])
                        npc_health.remove(npc_health[target])
                        command = '> '
                        target = 0
                        break

                if command.lower() not in fightCommandList:
                    NotRecognized(4)

    # Say
    if (command.lower()[:5]) == '/say ':
        said_word = (command[5:])
        print(f'You said: {said_word}')

    # Quit
    if command.lower() == 'quit':
        print('You disconnected your player. You died.')
        break

    # Flee Attempt
    if command.lower() == 'flee':
        print('You can only flee in combat.')

    # Died in Combat
    if command.lower() == 'wiheqw87wqzx54qw6e':
        break

    # If command is not recognized
    if (command.lower()[:5]) == '/say ':
        pass

    elif command.lower() not in commandlist:
        NotRecognized(4)

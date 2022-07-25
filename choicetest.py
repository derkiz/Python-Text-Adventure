command = input('left or right: ')

if command == 'right':
    print('you turn right. Straight into a hole and died.')
elif command == 'left':
    print('you turn left. through a small clearing in the forest.')

    command = input('A female dark elf appears, she is radiant. hi / walk away?')

    if command == 'hi':
        print('She slits your throat with a knife. You died.')
    elif command == 'walk away':
        print('You walk away from the dark elf.')

        command = input('The forest gets deeper. go back or continue?')

        if command == 'go back':
            print('As you begin to turn back you feel a blade slit your throat. You died.')
        elif command == 'continue':
            print('You continue through the bushes and find a sword. Pick it up? Yes / No')
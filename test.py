# Ignore This File

import names
import random

def gen_npcs():

    name = []
    hp = 100

    while len(name) < 10:
        random_int = random.randint(1, 10)
        if random_int < 8:
            minus_hp_ran = 0
        else:
            minus_hp_ran = random.randint(1, 55)
        name.append((names.get_full_name(), hp - minus_hp_ran))

    print(name)

gen_npcs()
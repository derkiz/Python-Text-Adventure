import random
import names

# Generate 10 NPCs onto a list.

npc_list = []

def gen_list():

    hp = 100

    while len(npc_list) < 10:
        random_int = random.randint(1, 10)
        if random_int < 8:
            minus_hp_ran = 0
        else:
            minus_hp_ran = random.randint(1, 55)
        npc_list.append((names.get_full_name(), hp - minus_hp_ran))

gen_list()

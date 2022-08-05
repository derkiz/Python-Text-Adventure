import random
import names

# Generate 10 NPCs onto a list.

npc_list = []
npc_health = []
npc_corpse = []


def gen_npc():

    while len(npc_list) < 10:
        npc_list.append(names.get_full_name())

    print(npc_list)


def gen_hp():

    hp = 100

    while len(npc_health) < 10:
        random_int = random.randint(1, 10)
        if random_int < 8:
            minus_hp_ran = 0
        else:
            minus_hp_ran = random.randint(1, 55)
        npc_health.append(hp - minus_hp_ran)

    print(npc_health)


gen_npc()
gen_hp()

# gen_hp()

import random
import names

# Generate 10 NPCs onto a list.

gen_npc_amount = 5

npc_list = []
npc_health = []
npc_corpse = []


def gen_npc():

    while len(npc_list) < gen_npc_amount:
        npc_list.append(names.get_full_name())


def gen_hp():

    hp = 100

    while len(npc_health) < gen_npc_amount:
        random_int = random.randint(1, 10)
        if random_int < 8:
            minus_hp_ran = 0
        else:
            minus_hp_ran = random.randint(1, 55)
        npc_health.append(hp - minus_hp_ran)


gen_npc()
gen_hp()

# gen_hp()

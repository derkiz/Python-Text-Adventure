import random
import names

# Generate 10 NPCs onto a list.

gen_npc_amount = 5


npc_list = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
npc_health = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
npc_corpse = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]


def gen_npc():

    n = 0

    while n < 9:

        while len(npc_list[n]) < gen_npc_amount:
            npc_list[n].append(names.get_full_name())

        n += 1

    print(npc_list)


def gen_hp():

    n = 0

    while n < 9:

        hp = 100

        while len(npc_health[n]) < gen_npc_amount:
            random_int = random.randint(1, 10)
            if random_int < 8:
                minus_hp_ran = 0
            else:
                minus_hp_ran = random.randint(1, 55)
            npc_health[n].append(hp - minus_hp_ran)

        n += 1

    print(npc_health)


gen_npc()
gen_hp()

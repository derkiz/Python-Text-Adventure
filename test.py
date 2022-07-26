# Ignore This File

import random
from modules import *
from generateplayers import *

print(gen_list)

target = 5

command = input('> ')

if command.lower() == 'print target':
    print(gen_list[target-1])

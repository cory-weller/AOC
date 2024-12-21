#!/usr/bin/env python

#infilename = 'input.txt'
infilename = 'tiny.txt'

import re

with open(infilename, 'r', encoding='UTF-8') as infile:
    text = infile.read().split('\n\n')

N_machines = len(text)
coordpattern = re.compile('[XY][+=][0-9]+')
machines = {}
for n,i in enumerate(text):
    results= [int(x[2:]) for x in re.findall(string=i, pattern=coordpattern)]
    machines[n] = {}
    machines[n]['A'] = results[0:2]
    machines[n]['B'] = results[2:4]
    machines[n]['prize'] = [x+10000000000000 for x in  results[4:6]]


# A = 3 token
# B = 1 token

# Iterate combinations and if X pos is good, then check y

def gen_combos(machine):
    ax, ay = machine['A']
    bx, by = machine['B']
    px, py = machine['prize']    
    ax, ay, bx, by, px, py
    for a in range(1,101):
        for b in range(1,101):
            if a*ax + b*bx == px:
                if a*ay + b*by == py:
                    yield (a,b,3*a+b)


cost = 0

for key in list(machines.keys()):
    winning_combos = list(gen_combos(machines[key]))
    if len(winning_combos) == 0:
        continue
    min_cost = min([x[2] for x in winning_combos])
    cost += min_cost


print(cost)


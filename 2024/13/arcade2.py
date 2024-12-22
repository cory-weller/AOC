#!/usr/bin/env python

infilename = 'input.txt'
#infilename = 'tiny.txt'

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



# Solve A and B by systems of equations
def get_AB(machine):
    ax, ay = machine['A']
    bx, by = machine['B']
    px, py = machine['prize']
    # If both same slope:
    if ay/ax == by/bx:
        print('Uhoh same slope')
    A = (px*by - py*bx) / (ax*by - ay*bx)
    B = (px - ax*A)/bx
    if A%1 == 0 and B%1 == 0:
        return (A,B)
    else:
        return (None, None)



cost = 0
for i in list(machines.keys()):
    A,B = get_AB(machines[i])
    if A and B:
        cost += 3*A
        cost += B

print(cost)
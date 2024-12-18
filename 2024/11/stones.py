#!/usr/bin/env python3

infilename = 'input.txt'

with open(infilename, 'r', encoding='UTF-8') as infile:
    start = infile.read().strip().split()
    start = [int(x) for x in start]


def mutate(x):
    if x==0:
        return([1])
    xstr = str(x)
    if len(xstr)%2 == 0:
        mid = int(len(xstr)/2)
        first = int(xstr[:mid])
        second = int(xstr[mid:])
        return([first, second])
    else:
        return([2024*x])


blinks = 75


# Initialize stones dict
stones = {}
for i in start:
    if i not in stones:
        stones[i] = 1
    else:
        stones[i] += 1


for n in range(blinks):
    next_layer = {}
    for i in stones.keys():
        count = stones[i]
        new_stones = mutate(i)
        for j in new_stones:
            try: next_layer[j] += count
            except KeyError: next_layer[j] = count
    stones = next_layer

total = 0

for i in stones:
    total += stones[i]

print(total)


exit()
#!/usr/bin/env python3

# infilename = 'tiny.txt'
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

def flatten(nested_list):
    return [x for lists in nested_list for x in lists]

blinks = 75

for i in range(blinks):
    #print(start)
    start = flatten([mutate(x) for x in start])
    print(len(set(start)))

while True:
    i = max(start)
    print(i)
    start = mutate(i)


# Part 2


count = 0
def recursive_mutate(N, blinks, max_blinks):
    global count
    if blinks >= max_blinks:
        count += 1
    else:
        for i in mutate(N):
            recursive_mutate(i, blinks+1, max_blinks)


for i in start[1:2]:
    recursive_mutate(N=i, blinks=0, max_blinks=40)

print(count)


branches = {}

for i in range(10):
    for mb in range(50):
        count = 0
        recursive_mutate(N=i, blinks=0, max_blinks=mb)




print(count)


    

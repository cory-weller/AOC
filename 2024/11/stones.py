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
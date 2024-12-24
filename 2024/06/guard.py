#!/usr/bin/env python

#infilename = 'tiny.txt'
infilename = 'input.txt'

import numpy as np

with open(infilename, 'r', encoding='UTF-8') as infile:
    text = infile.readlines()
    text = [list(x.strip()) for x in text]

grid = np.array([x for x in text])

def new_direction(direction):
    directions = {  '^':'>',
                    '>':'v',
                    'v':'<',
                    '<':'^'
                    }
    return directions[direction]


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i,j] in ['^','>','v','<']:
            direction = grid[i,j]
            starting_pos = (i,j)


i,j = starting_pos

grid[i,j] = 'X'


def get_LOS(grid, i, j, direction):
    if direction == '^':
        view = grid[:i, j][::-1]
    elif direction == '>':
        view = grid[i, j+1:]
    elif direction == 'v':
        view = grid[i+1:, j]
    elif direction == '<':
        view = grid[i, :j][::-1]
    count = 0
    for n,x in enumerate(view):
        if x != '#':
            view[n] = 'X'
            count += 1
        elif x == '#':
            break
    if direction == '^':
        i -= count
    elif direction == '>':
        j += count
    elif direction == 'v':
        i += count
    elif direction == '<':
        j -= count
    return(i,j)

max_i = len(grid)-1
max_j = len(grid[0])-1

def finished(i,j,direction,max_i, max_j):
    if direction == '^' and i == 0:
        return True
    if direction == '>' and j == max_j:
        return True
    if direction == 'v' and i == max_i:
        return True
    if direction == '<' and j == 0:
        return True


while True:
    i,j = get_LOS(grid, i, j, direction)
    if finished(i,j,direction,max_i,max_j):
        break
    else:
        direction = new_direction(direction)


count = 0
for x in grid:
    count += sum([1 for y in x if y=='X'])

print(count)

#!/usr/bin/env python

#infilename = 'tiny.txt'
infilename = 'input.txt'

import numpy as np

def new_direction(direction):
    directions = {  '^':'>',
                    '>':'v',
                    'v':'<',
                    '<':'^'
                    }
    return directions[direction]

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

def finished(i,j,direction,max_i, max_j):
    if direction == '^' and i == 0:
        return True
    if direction == '>' and j == max_j:
        return True
    if direction == 'v' and i == max_i:
        return True
    if direction == '<' and j == 0:
        return True

with open(infilename, 'r', encoding='UTF-8') as infile:
    text = infile.readlines()
    text = [list(x.strip()) for x in text]

grid = np.array([x for x in text])


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i,j] in ['^','>','v','<']:
            direction = grid[i,j]
            starting_pos = (i,j)

i,j = starting_pos

grid[i,j] = 'X'

max_i = len(grid)-1
max_j = len(grid[0])-1
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

visited_positions = {}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i,j] == 'X':
            visited_positions[(i,j)] = {}


import copy
positions_to_test = list( visited_positions.keys())

# Reset grid to original position


with open(infilename, 'r', encoding='UTF-8') as infile:
    text = infile.readlines()
    text = [list(x.strip()) for x in text]

grid = np.array([x for x in text])


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i,j] in ['^','>','v','<']:
            direction = grid[i,j]
            starting_pos = (i,j)

i,j = starting_pos

grid[i,j] = 'X'


def test_obstruction(orig_grid, starting_pos, obstruction_pos, direction, abort_count):
    grid = copy.deepcopy(orig_grid)
    i,j = starting_pos
    grid[obstruction_pos] = '#'
    count = 0
    while True:
        i,j = get_LOS(grid, i, j, direction)
        count += 1
        if count >= abort_count:
            return 1
        if finished(i,j,direction,max_i,max_j):
            return 0
        else:
            direction = new_direction(direction)



tests = []
for x in positions_to_test:
    result = test_obstruction(grid, starting_pos, x, direction, 20000)
    tests.append(result)

print(sum(tests))



#!/usr/bin/env python3

# infilename = 'tiny.txt'
infilename = 'input.txt'

with open(infilename, 'r', encoding='UTF-8') as infile:
    grid = infile.readlines()
    grid = [list(x.strip()) for x in grid]

for i in grid:
    print(''.join(i))

def get_characters(grid):
    chars = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            char = grid[i][j]
            if char == '.':
                continue
            if char in chars:
                chars[char].append((i,j))
            else:
                chars[char] = [(i,j)]
    return chars

chars = get_characters(grid)

def get_antinodes(node_1, node_2, max_i, max_j, extend=False):
    def in_bounds(node, max_i, max_j):
        if node[0] < 0 or node[0] > max_i:
            return False
        if node[1] < 0 or node[1] > max_j:
            return False
        else:
            return True
    output = []
    if extend:
        N = range(50)
    else:
        N = [1]
    for n in N:
        dy = node_1[0] - node_2[0]
        dx = node_1[1] - node_2[1]
        antinode_1 = (node_1[0] + dy*n, node_1[1] + dx*n )
        antinode_2 = (node_2[0] - dy*n, node_2[1] - dx*n )
        for node in [antinode_1, antinode_2]:
            if in_bounds(node, max_i, max_j):
                output.append(node)
    return output


max_i = len(grid) - 1
max_j = len(grid[0]) - 1

import itertools

# Get part 1
antinodes = []

for char in list(chars.keys()):
    combos = itertools.combinations(chars[char], r=2)
    for combo in combos:
        for x in get_antinodes(combo[0], combo[1], max_i, max_j):
            if x not in antinodes:
                antinodes.append(x)

print(len(antinodes))

# Get part 2
antinodes = []

for char in list(chars.keys()):
    combos = itertools.combinations(chars[char], r=2)
    for combo in combos:
        for x in get_antinodes(combo[0], combo[1], max_i, max_j, extend=True):
            if x not in antinodes:
                antinodes.append(x)

print(len(antinodes))
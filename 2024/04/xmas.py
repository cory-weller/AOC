#!/usr/bin/env python3

with open('input.txt', 'r', encoding='UTF-8') as infile:
    m = infile.read()

m = m.split('\n')

import re


def get_diagonal(M:list) -> list:
    nrow = len(M)
    ncol = len(M[0])
    mydict = {}
    for i in range(nrow):
        for j in range(ncol):
            try: mydict[j-i] += M[i][j]
            except: mydict[j-i] = M[i][j]
    output = [mydict[x] for x in mydict]
    return output


def count_xmas(M:list) -> int:
    N = len(re.findall(pattern = 'XMAS', string=' '.join(M)))
    return N


def rotate_clockwise(M:list) -> list:
    nrow = len(M)
    ncol = len(M[0])
    newlist = [''] * nrow
    for i in reversed(range(nrow)):
        for j in reversed(range(ncol)):
            newlist[j] += M[i][j]
    return newlist


counts = 0
for i in range(4):
    counts += count_xmas(m)
    counts += count_xmas(get_diagonal(m))
    m = rotate_clockwise(m)

print(counts)

# Part two


with open('input.txt', 'r', encoding='UTF-8') as infile:
    m = infile.read()

m = m.split('\n')

nrow = len(m)
rows = range(nrow)
ncol = len(m[0])
cols = range(ncol)





directions = ['N','NE','E','SE','S','SW','W','NW']


xs = []
for x in rows:
    for y in cols:
        if m[x][y] == 'X':
            xs.append((x,y))

for start_pos in xs:
    for direction in directions:

check_xmas(start_pos, direction='N')

def check_pos(m, startpos, needchar):
    start_x = startpos[0]
    start_y = startpos[1]

    # Get 


def get_next_positions(startpos, m):
    nrow = len(m)
    ncol = len(m[0])
    start_x = startpos[0]
    start_y = startpos[1]
    next_positions = []
    for x_mod in [-1, 0, 1]:
        for y_mod in [-1, 0, 1]:
            if not (x_mod == 0 and y_mod == 0):
                new_x = start_x + x_mod
                new_y = start_y + y_mod
                if new_x >= 0 and new_x < nrow - 1:
                    if new_y >= 0 and new_y < ncol - 1:
                        next_positions.append([new_x, new_y])
    return(next_positions)

for x in range(nrow):
    for y in range(ncol):
        if m[x][y] == 'X':
            next_positions = get_next_positions([x,y], m)
            # Problem: no memory of the direction we're going with next positions.
            # Need to remember in order to keep extending same direction


# get_next_positions([0,0], m)


# check_xmas(direction)
#     nexts = {None:'X','X':'M', 'M':'A','A':'S', 'S':None}
#     next_char = nexts[previous_character]


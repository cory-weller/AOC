#!/usr/bin/env python

# infilename = 'tiny.txt'
infilename = 'input.txt'

with open(infilename, 'r', encoding='UTF-8') as infile:
    m = infile.read()

m = m.split('\n')


def get_crosses(grid, i, j):
    mid = grid[i][j]
    try: left = [grid[i-1][j-1], mid, grid[i+1][j+1]]
    except IndexError: left = None
    try: right = [grid[i+1][j-1], mid, grid[i-1][j+1]]
    except IndexError: right = None
    return (left, right)

def is_xmas(mylist):
    if mylist == ['M','A','S'] or mylist == ['S','A','M']:
        return True


count = 0
for i in range(1,len(m)-1):
    for j in range(1, len(m[0])-1):
        left, right = get_crosses(m, i, j)
        print(i, j, left, right)
        if is_xmas(left) and is_xmas(right):
            count += 1


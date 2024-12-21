#!/usr/bin/env python

infilename = 'input.txt'

with open(infilename, 'r', encoding='UTF-8') as infile:
    garden = [list(x.strip()) for x in infile.readlines() if x != '']


def getPlot(garden):
    area = 0
    perimeter = 0
    def search(garden, i, j, letter):
        nonlocal perimeter
        nonlocal area
        # If current cell is a fence for given letter
        if i < 0 or i >= len(garden) or j < 0 or j >= len(garden[0]):
            perimeter += 1
            return None
        if garden[i][j] == '*':
            return None
        if garden[i][j] != letter:
            perimeter += 1
            return None
        # set as '*' after checking, increment area
        garden[i][j] = '*'
        area += 1
        
        # search adjacent positions
        search(garden, i + 1, j, letter)
        search(garden, i - 1, j, letter)
        search(garden, i, j + 1, letter)
        search(garden, i, j - 1, letter)
        
    def get_new_letter(garden):
        for i in range(len(garden)):
            for j in range(len(garden[0])):
                test_letter = garden[i][j]
                if test_letter != '_' and test_letter != '*':
                    letter = garden[i][j]
                    return (i,j,letter)
    
    i, j, letter = get_new_letter(garden)
    search(garden, i, j, letter)
    return (area, perimeter)

# Turn '*' into '_' for completed plot
def resetGarden(garden):
    newgarden = [['_' if x=='*' else x for x in y] for y in garden]
    if newgarden == garden:
        return None
    else:
        return newgarden

# For viewing/debug
def printGarden(garden):
    for i in garden:
        print(''.join(i))

def check_neighbor(garden, i, j):
    # If cell is a fence for given letter
    if i < 0 or j < 0:
        return False
    try: result = (garden[i][j] == '*')
    except IndexError: result = False
    return result

def count_crosses(garden):
    crosses = 0
    for i in range(len(garden)-2):
        for j in range(len(garden[0])-2):
            a = check_neighbor(garden, i, j)
            b = check_neighbor(garden, i, j+1)
            c = check_neighbor(garden, i+1, j)
            d = check_neighbor(garden, i+1, j+1)
            neighbors = a + b + c + d
            if neighbors == 2:
                if (a and d) or (b and c):
                    crosses += 1
    return crosses

def count_corners(garden):
    corners = 0
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            letter = garden[i][j]
            down = check_neighbor(garden, i+1, j)
            right = check_neighbor(garden, i, j+1)
            up = check_neighbor(garden, i-1, j)
            left = check_neighbor(garden, i, j-1)
            neighbors = down + right + up + left
            corridor = neighbors == 2 and ( (down and up) or (left and right) )
            if corridor:
                continue
            if letter == '*':
                if neighbors == 2:
                    corners += 1
                elif neighbors == 1:
                    corners += 2
                elif neighbors == 0:
                    corners += 4
            elif garden[i][j] != '*':   # check internal corners
                if neighbors == 4:
                    corners += 4
                elif neighbors == 3:
                    corners += 2
                elif neighbors == 2:
                    corners += 1
    return corners

values = []



# Iterate until done
while garden is not None:
    if len(values) > 0:
        garden = resetGarden(garden)
    try: area_perimeter = getPlot(garden)
    except: break
    corners = count_corners(garden)
    corners -= 2*count_crosses(garden)
    area = area_perimeter[0]
    values.append((area, corners))
    


total = sum([x[0]*x[1] for x in values])
print(total)

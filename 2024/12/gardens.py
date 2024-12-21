#!/usr/bin/env python

infilename = 'input.txt'
#infilename = 'tiny.txt'

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

values = []

# Iterate until done
while garden is not None:
    if len(values) > 0:
        garden = resetGarden(garden)
    #printGarden(garden)
    try: area_perimeter = getPlot(garden)
    except: break
    values.append(area_perimeter)


total = sum([x[0]*x[1] for x in values])
print(total)


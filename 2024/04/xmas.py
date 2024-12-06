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
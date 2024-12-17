#!/usr/bin/env python

infilename = 'input.txt'
#infilename = 'tiny.txt'

import itertools
import numpy as np
import re

with open(infilename, 'r', encoding='UTF-8') as infile:
    data = infile.readlines()
    data = [x.strip() for x in data]


if infilename == 'tiny.txt':
    width = 11
    height = 7
elif infilename == 'input.txt':
    width = 101
    height = 103


x_starts = []
x_velocities = []
y_starts = []
y_velocities = []



for i in data:
    p, v = i[2:].replace('v=','').split()
    p_x, p_y = [int(x) for x in p.split(',')]
    v_x, v_y = [int(x) for x in v.split(',')]
    x_starts.append(p_x)
    x_velocities.append(v_x)
    y_starts.append(p_y)
    y_velocities.append(v_y)


def generate_robot_map(x, xv, y, yv, height, width):
    x = np.array(x)
    xv = np.array(xv)
    y = np.array(y)
    yv = np.array(yv)
    while True:
        x = np.add(x, xv)
        x = np.mod(x, width)
        y = np.add(y, yv)
        y = np.mod(y, height)
        yield(list(zip(y,x)))


def get_robots(positions, height, width):
    mat = np.zeros(shape=(height,width))
    for i in positions:
        mat[i] += 1
    return(mat)


def print_robots(mat):
    mat = [''.join(' ' if x == 0 else '&' for x in y) for y in mat]
    print('\n'.join(mat))




maps = generate_robot_map(x=x_starts,
                            xv=x_velocities,
                            y=y_starts,
                            yv=y_velocities,
                            height=height,
                            width=width)



desired = 100

a = next(itertools.islice(maps, desired-1, None))
robots = get_robots(a, height, width)

mid_x = int((width-1)/2)
mid_y = int((height-1)/2)

q1 = robots[:mid_y, :mid_x]
q2 = robots[0:mid_y, 1+mid_x:]
q3 = robots[1+mid_y:, 0:mid_x]
q4 = robots[1+mid_y:, 1+mid_x:]

result = np.sum(q1) * np.sum(q2) * np.sum(q3) * np.sum(q4)
result = int(result)
print(result)

# Part Two
maps = generate_robot_map(x=x_starts,
                            xv=x_velocities,
                            y=y_starts,
                            yv=y_velocities,
                            height=height,
                            width=width)


counter = 0
for i in maps:
    counter += 1
    if counter > 100000:
        break
    robots = get_robots(i, height, width)
    rowsums = robots.sum(axis=1)  # row sums
    colsums = robots.sum(axis=0)  # column sums
    if max(rowsums) > 30:
        if max(colsums) > 30:
            print_robots(robots)
            print(counter, max(rowsums), max(colsums))
            break


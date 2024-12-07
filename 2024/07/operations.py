#!/usr/bin/env python3

# Part one

with open('input.txt', 'r', encoding='UTF-8') as infile:
    input = [x.strip() for x in infile.readlines()]


input = [[int(y) for y in sublist] for sublist in [x.replace(':','').split() for x in input]]

import itertools

def check_products(vals:list, options='*+'):
    desired_total = vals[0]
    vals = vals[1:]
    operation_combos = itertools.product(options, repeat=len(vals)-1)
    for combo in operation_combos:
        count = vals[0]
        for i, operation in zip(vals[1:], combo):
            if operation == '*':
                count *= i
            elif operation == '+':
                count += i
        if count == desired_total:
            return count
    return 0

totals = 0
for i in input:
    totals += check_products(i)

print(totals)


# Part two

with open('input.txt', 'r', encoding='UTF-8') as infile:
    input = [x.strip() for x in infile.readlines()]

input = [[int(y) for y in sublist] for sublist in [x.replace(':','').replace('||','|').split() for x in input]]

def check_products_2(vals:list, options='*+|'):
    desired_total = vals[0]
    vals = vals[1:]
    operation_combos = itertools.product(options, repeat=len(vals)-1)
    for combo in operation_combos:
        count = vals[0]
        for i, operation in zip(vals[1:], combo):
            if operation == '*':
                count *= i
            elif operation == '+':
                count += i
            elif operation == '|':
                count = int(str(count) + str(i))
        if count == desired_total:
            return count
    return 0

totals = 0
for i in input:
    totals += check_products_2(i)

print(totals)


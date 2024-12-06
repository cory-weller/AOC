#!/usr/bin/env python3

# Part one

def read_file(filename:str):
    with open(filename, 'r', encoding='UTF-8') as infile:
        for line in infile:
            levels = line.strip().split()
            levels = [int(x) for x in levels]
            yield levels

def is_safe(report: list) -> bool:
    if report != sorted(report) and report != list(reversed(sorted(report))):
        return False
    for i in range(len(report)-1):
        pair = report[i:(i+2)]
        if pair[1] == pair[0]:
            return False
        if abs(pair[1] - pair[0]) > 3:
            return False
    return True
        

reports = read_file('input.txt')

count = 0
for report in reports:
    if is_safe(report):
        count += 1
        print(report)

print(count)

# Part two


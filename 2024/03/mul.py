#!/usr/bin/env python3

import re

with open('input.txt', 'r', encoding='UTF-8') as infile:
    text = ''.join([x.strip() for x in infile.readlines()])

matches = re.findall(pattern='mul\\([0-9]+,[0-9]+\\)', string=text)

count = 0
for i in matches:
    vals = re.split('\\(|,|\\)', i)[1:3]
    product = int(vals[0]) * int(vals[1])
    count += product

print(count)

# Part two

# prefix with ON and end with OFF
text = 'do()' + text + "don't()"

# get good sections
good_parts = re.findall(pattern="do\\(\\).*?don't\\(\\)", string=text)


count = 0

for i in good_parts:
    matches = re.findall(pattern='mul\\([0-9]+,[0-9]+\\)', string=i)
    for match in matches:
        vals = re.split('\\(|,|\\)', match)[1:3]
        product = int(vals[0]) * int(vals[1])
        count += product

print(count)
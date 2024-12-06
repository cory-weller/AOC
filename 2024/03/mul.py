#!/usr/bin/env python3

import re

with open('input.txt', 'r', encoding='UTF-8') as infile:
    text = ''.join([x.strip() for x in infile.readlines()])

matches = re.findall(pattern='mul\\([0-9]+,[0-9]+\\)', string=text)

count = 0
for i in matches:
    print(i)
    vals = re.split('\\(|,|\\)', i)[1:3]
    product = int(vals[0]) * int(vals[1])
    print(product)
    count += product

print(count)
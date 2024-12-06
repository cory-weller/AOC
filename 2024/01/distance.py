#!/usr/bin/env python3

## Part one

with open('input.txt', 'r', encoding='UTF-8') as infile:
    text = [x.strip() for x in infile.readlines()]

left = [int(x.split()[0]) for x in text]
left.sort()

right = [int(x.split()[1]) for x in text]
right.sort()

distances = [abs(i[0] - i[1]) for i in zip(left, right)]

print(sum(distances))


## Part two

similarity_score = [i * right.count(i) for i in left]
print(sum(similarity_score))
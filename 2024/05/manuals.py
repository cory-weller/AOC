#!/usr/bin/env python3

with open('input.txt', 'r', encoding='UTF-8') as infile:
    rules, updates = infile.read().split('\n\n')

rules = rules.strip().split()
rules = [x.split('|') for x in rules]
rules = [[int(y) for y in x] for x in rules]


updates = updates.strip().split()
updates = [x.split(',') for x in updates]
updates = [[int(y) for y in x] for x in updates]

for page in update:


unique_pages = list(set([x for sublist in updates for x in sublist]))

relevant_rules = {}
for page in unique_pages:
    for rule in rules:
        if page in rule:
            try: relevant_rules[page].append(rule)
            except: relevant_rules[page] = [rule]

def get_rules(mydict, rule_list):
    output = []
    for rule in rule_list:
        output.append(mydict[rule])
    return list(set(output))

for update in updates:
    
#!/usr/bin/env python3

with open('input.txt', 'r', encoding='UTF-8') as infile:
    rules, updates = infile.read().split('\n\n')

rules = rules.strip().split()
rules = [x.split('|') for x in rules]
rules = [[int(y) for y in x] for x in rules]


updates = updates.strip().split()
updates = [x.split(',') for x in updates]
updates = [[int(y) for y in x] for x in updates]

unique_pages = list(set([x for sublist in updates for x in sublist]))

relevant_rules = {}
for page in unique_pages:
    for rule in rules:
        if page in rule:
            try: relevant_rules[page].append(rule)
            except: relevant_rules[page] = [rule]

# def get_rules(mydict, rule_list):
#     output = []
#     for rule in rule_list:
#         output.append(mydict[rule])
#     return list(set(output))

def order_ok(update, relevant_rules):
    for i in update:
        rules = relevant_rules[i]
        for rule in rules:
            if rule[0] not in update or rule[1] not in update:
                continue
            if not update.index(rule[0]) < update.index(rule[1]):
                return None
    return update

good_updates = []
for update in updates:
    if order_ok(update, relevant_rules):
        good_updates.append(update)

def get_middle(mylist):
    l = len(mylist)
    assert l%2 == 1, 'rule list is not odd'
    middle = mylist[int((l-1)/2)]
    return(middle)

count = 0
for i in good_updates:
    count += get_middle(i)

print(f'Middle sum of good updates: {count}')

# Part two
bad_updates = [x for x in updates if x not in good_updates]

def fix_update(bad_update, relevant_rules):
    reordered_update = [bad_update[0]]
    for val in bad_update[1:]:
        for i in range(len(reordered_update)+1):
            order_to_try = reordered_update[:i] + [val] + reordered_update[i:]
            if order_ok(order_to_try, relevant_rules):
                reordered_update = order_to_try
                break
    return(reordered_update)


update = bad_updates[0]
fix_update(update, relevant_rules)

fixed_updates = []
for bad_update in bad_updates:
    fixed_updates.append(fix_update(bad_update, relevant_rules))

count = 0
for i in fixed_updates:
    count += get_middle(i)

print(f'Middle sum of fixed bad updates: {count}')
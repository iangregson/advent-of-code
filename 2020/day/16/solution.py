#!/usr/bin/env python3

import os
from collections import namedtuple, defaultdict
from itertools import groupby
from functools import reduce
from operator import mul

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/day16_input.txt", "r")
lines = [l.strip() for l in file.readlines()]

raw_rules = lines[0:20]
my_ticket = lines[22]
other_tickets = lines[25:]

# lines = [
#   'class: 1-3 or 5-7',
#   'row: 6-11 or 33-44',
#   'seat: 13-40 or 45-50',
#   '',
#   'your ticket:',
#   '7,1,14',
#   '',
#   'nearby tickets:',
#   '7,3,47',
#   '40,4,50',
#   '55,2,20',
#   '38,6,12',
# ]

# rules = lines[0:3]
# my_ticket = lines[5]
# other_tickets = lines[8:]


# print(rules)
# print(my_ticket)
# print(other_tickets)

# lines = [
#   'class: 0-1 or 4-19',
#   'row: 0-5 or 8-19',
#   'seat: 0-13 or 16-19',
#   '',
#   'your ticket:',
#   '11,12,13',
#   '',
#   'nearby tickets:',
#   '3,9,18',
#   '15,1,5',
#   '5,14,9',
# ]

# rules = lines[0:3]
# my_ticket = lines[5]
# other_tickets = lines[8:]

# print(rules)
# print(my_ticket)
# print(other_tickets)

rules = []
for rule in raw_rules:
  field, ranges = rule.split(': ')
  r1, r2 = ranges.split(' or ')
  r1_low, r1_high = (int(x) for x in r1.split('-'))
  r2_low, r2_high = (int(x) for x in r2.split('-'))
  rules.append((field, r1_low, r1_high, r2_low, r2_high))

error_rate = 0
rules_count = len(rules)
# start with all rules (indexes) being valid for each column
cols = [set(range(rules_count)) for _ in range(rules_count)]

for ticket in other_tickets:
    valid_ticket = True
    ticket_rules = []

    for number in map(int, ticket.split(",")):
        matching_rules = set(
            i
            for i, (_, lo1, hi1, lo2, hi2) in enumerate(rules)
            if lo1 <= number <= hi1 or lo2 <= number <= hi2
        )
        if len(matching_rules) == 0:
            error_rate += number
            valid_ticket = False
        elif valid_ticket:
            ticket_rules.append(matching_rules)

    if valid_ticket:
        for col, matching_rules in zip(cols, ticket_rules):
            col &= matching_rules  # col is a reference, not a copy

print('Part 1:', error_rate)

total = 1
singles = set()
your_ticket = [int(number) for number in my_ticket.split(",")]
while len(singles) != rules_count:
    for i, col in enumerate(cols):
        if len(col) > 1:
            col -= singles
        elif len(col) == 1:
            singles |= col
            if rules[col.pop()][0].startswith("departure"):
                total *= your_ticket[i]

print('Part 2:', total)
#!/usr/bin/env python3

import os
from collections import defaultdict, Counter

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# print(lines)
lines = [
  'NNCB',
  '',
  'CH -> B',
  'HH -> N',
  'CB -> H',
  'NH -> C',
  'HB -> C',
  'HC -> B',
  'HN -> C',
  'NN -> C',
  'BH -> H',
  'NC -> B',
  'NB -> B',
  'BN -> B',
  'BB -> N',
  'BC -> B',
  'CC -> N',
  'CN -> C',
]

polymer_template = lines[0]
rules = dict(line.split(" -> ") for line in lines[2:])

def get_pairs(polymer):
  molecules = []
  for i in range(len(polymer) - 1):
    molecule = polymer[i:i+2]
    molecules.append(molecule)
  return molecules

def process_polymer(polymer, rules):
  molecules = []
  for molecule in get_pairs(polymer):
    if molecule in rules:
      molecule = molecule[0] + rules[molecule] + molecule[1]
    molecules.append(molecule)  

  new_polymer = molecules[0]
  for molecule in molecules[1:]:
    new_polymer += molecule[1:]

  return new_polymer

polymer = polymer_template
for step in range(10):
  polymer = process_polymer(polymer, rules)

print(len(polymer), Counter(polymer).most_common(), Counter(polymer).most_common()[0][1] - Counter(polymer).most_common()[-1][1])
  

letter_freq = Counter(polymer_template)
pair_freq = Counter(get_pairs(polymer_template))

for i in range(40):
  prev_pair_freq = pair_freq.copy()
  for pair, insertion in rules.items():
    count = prev_pair_freq[pair]
    pair_freq[pair] -= count
    pair_freq[pair[0] + insertion] += count
    pair_freq[insertion + pair[1]] += count
    letter_freq[insertion] += count
  if i == 9:
    print(letter_freq.most_common(), letter_freq.most_common()[0][1]-letter_freq.most_common()[-1][1])


print(letter_freq.most_common(), letter_freq.most_common()[0][1]-letter_freq.most_common()[-1][1])
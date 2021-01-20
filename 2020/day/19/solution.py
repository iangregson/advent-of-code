#!/usr/bin/env python3

import os
from collections import namedtuple, defaultdict
from itertools import takewhile

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '0: 4 1 5',
#   '1: 2 3 | 3 2',
#   '2: 4 4 | 5 5',
#   '3: 4 5 | 5 4',
#   '4: "a"',
#   '5: "b"',
#   '',
#   'ababbb',
#   'bababa',
#   'abbbab',
#   'aaabbb',
#   'aaaabbb',
# ]

# lines = [
#   '42: 9 14 | 10 1',
#   '9: 14 27 | 1 26',
#   '10: 23 14 | 28 1',
#   '1: "a"',
#   '11: 42 31',
#   '5: 1 14 | 15 1',
#   '19: 14 1 | 14 14',
#   '12: 24 14 | 19 1',
#   '16: 15 1 | 14 14',
#   '31: 14 17 | 1 13',
#   '6: 14 14 | 1 14',
#   '2: 1 24 | 14 4',
#   '0: 8 11',
#   '13: 14 3 | 1 12',
#   '15: 1 | 14',
#   '17: 14 2 | 1 7',
#   '23: 25 1 | 22 14',
#   '28: 16 1',
#   '4: 1 1',
#   '20: 14 14 | 1 15',
#   '3: 5 14 | 16 1',
#   '27: 1 6 | 14 18',
#   '14: "b"',
#   '21: 14 1 | 1 14',
#   '25: 1 1 | 1 14',
#   '22: 14 14',
#   '8: 42',
#   '26: 14 22 | 1 20',
#   '18: 15 15',
#   '7: 14 5 | 1 21',
#   '24: 14 1',
#   '',
#   'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
#   'bbabbbbaabaabba',
#   'babbbbaabbbbbabbbbbbaabaaabaaa',
#   'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
#   'bbbbbbbaaaabbbbaaabbabaaa',
#   'bbbababbbbaaaaaaaabbababaaababaabab',
#   'ababaaaaaabaaab',
#   'ababaaaaabbbaba',
#   'baabbaaaabbaaaababbaababb',
#   'abbbbabbbbaaaababbbbbbaaaababb',
#   'aaaaabbaabaaaaababaa',
#   'aaaabbaaaabbaaa',
#   'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
#   'babaaabbbaaabaababbaabababaaab',
#   'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
# ]

space_idx = lines.index('')
rule_lines = lines[:space_idx]
msg_lines = lines[space_idx+1:]

rules = {}

for line in rule_lines:
  key, rule = line.split(': ')
  rules[int(key)] = rule

def consume(msg, rule_number, rules):
  rule = rules[rule_number]

  # handle terminal case
  if rule[0] == '"':
    rule = rule.strip('"')
    if msg.startswith(rule):
      return [len(rule)]
    else:
      return []
  else:
    total = []
    for option in rule.split(' | '):
      acc = [0]
      for rule_n in [int(x) for x in option.split(' ')]:
        local_acc = []
        for x in acc:
          result = consume(msg[x:], rule_n, rules)
          for y in result:
            local_acc.append(x + y)
        acc = local_acc
      total += acc
    return total

  return -1

n_good_msgs = 0
for msg in msg_lines:
  n_good_msgs += len(msg) in consume(msg, 0, rules)

print('Part 1:', n_good_msgs)

new_rules = rules.copy()
new_rules[8] = '42 | 42 8'
new_rules[11] = '42 31 | 42 11 31'

n_good_msgs = 0
for msg in msg_lines:
  n_good_msgs += len(msg) in consume(msg, 0, new_rules)

print('Part 2:', n_good_msgs)
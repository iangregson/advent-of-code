#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
#   'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
#   'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
#   'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
#   'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
#   'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
#   'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
#   'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
#   'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
#   'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
# ]

lines = [l.split(' | ') for l in lines]

n_segments_to_digits = {
  2: 1,
  4: 4,
  3: 7,
  7: 8,
}

counter = {
  1: 0,
  4: 0,
  7: 0,
  8: 0,
}
for l in lines:
  pattern, output = l
  digits = output.split()
  for d in digits:
    if len(d) in n_segments_to_digits.keys():
      counter[n_segments_to_digits[len(d)]] += 1

print(counter, sum(counter.values()))

def has_overlap(token1, token2):
  return len(set(token2).intersection(token1)) == len(token1)

def n_overlaps(token1, token2):
  return len(set(token2).intersection(token1))

def pattern_to_digit(tokens, pattern):
  tokens_by_length = {}
  for t in tokens:
    tokens_by_length[len(t)] = t
  if len(pattern) in n_segments_to_digits.keys():
    return n_segments_to_digits[len(pattern)]
  else:
    if len(pattern) == 6:
      # must be 0, 6 or 9
      if not has_overlap(tokens_by_length[2], pattern):
        return 6
      elif has_overlap(tokens_by_length[4], pattern):
        return 9
      else:
        return 0
    elif len(pattern) == 5:
      # must be 5, 3 or 2
      if has_overlap(tokens_by_length[2], pattern):
        return 3
      elif n_overlaps(tokens_by_length[4], pattern) == 3:
        return 5
      else:
        return 2
    return None

output_values = []
for l in lines:
  input_pattern, output = l
  tokens = input_pattern.split()
  digits = [pattern_to_digit(tokens, d) for d in output.split()]
  # print(f"{output}: {digits}")
  output_values.append(int("".join(map(str, digits))))

print(sum(output_values))
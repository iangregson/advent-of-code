#!/usr/bin/env python3

import os
from collections import defaultdict, Counter, deque, namedtuple
from enum import Enum
import itertools
import functools
import operator
import random
import ast
import math
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def add(pair1, pair2):
  return [pair1, pair2]

def reduce(pair):
  n_pair, exploded = explode(pair)
  if exploded:
    return reduce(n_pair)
  else:
    n_pair, is_split = split(pair)
    if is_split:
      return reduce(n_pair)
    else:
      return pair


def explode(pair):
  pair_str = str(pair).replace(' ', '')
  atoms = []
  i = 0
  while i < len(pair_str):  
    if pair_str[i] == '[':
      atoms.append(pair_str[i])
      i += 1
    elif pair_str[i] == ']':
      atoms.append(pair_str[i])
      i += 1
    elif pair_str[i] == ',':
      atoms.append(pair_str[i])
      i += 1
    else:
      assert pair_str[i].isdigit()
      j = i
      while j < len(pair_str) and pair_str[j].isdigit():
        j += 1
      atoms.append(int(pair_str[i:j]))
      i = j
  
  # atoms is a tree, depth increases on [ and decreases on ]
  depth = 0
  for i, a in enumerate(atoms):
    if a == '[':
      depth += 1
      if depth == 5:
        # this pair should be integers
        l, comma, r = atoms[i+1:i+4]
        assert(isinstance(l, int))
        assert(isinstance(r, int))
        assert(comma == ',')
        # explode the pair, find left and right siblings
        l_sibling_idx = None
        r_sibling_idx = None
        a, b = i-1, i+4
        while a >= 0:
          if isinstance(atoms[a], int):
            l_sibling_idx = a
            break
          a -= 1
        while b < len(atoms):
          if isinstance(atoms[b], int):
            r_sibling_idx = b
            break
          b += 1

        if l_sibling_idx is not None:
          atoms[l_sibling_idx] += l
        if r_sibling_idx is not None:
          atoms[r_sibling_idx] += r

        atoms = atoms[:i] + [0] + atoms[i+5:]
        return ast.literal_eval("".join([str(a) for a in atoms])), True
    if a == ']':
      depth -= 1
    else:
      pass

  return pair, False

def split(pair):
  # depth first recursion, preferring the left
  if isinstance(pair, list):
    new_pair_l, did_split = split(pair[0])
    if did_split == True:
      return [new_pair_l, pair[1]], True
    else:
      new_pair_r, did_split = split(pair[1])
      return [new_pair_l, new_pair_r], did_split
  else:
    assert(isinstance(pair, int))
    if pair >= 10:
      pair = [math.floor(pair/2), math.ceil(pair/2)]
      return pair, True
    else:
      return pair, False

def add_lines(lines):
  lines = [ast.literal_eval(l) for l in lines]
  sum = lines[0]
  for line in lines[1:]:
    sum = add(sum, line)
    sum = reduce(sum)
  return sum

def magnitude(pair):
  if isinstance(pair, list):
    return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])
  else:
    assert(isinstance(pair, int))
    return pair

def run_tests():
    x = ast.literal_eval("[1,2]")
    y = ast.literal_eval("[[3,4],5]")
    assert add(x, y) == ast.literal_eval("[[1,2],[[3,4],5]]")

    x, did_explode = explode(ast.literal_eval("[[[[[9,8],1],2],3],4]"))
    assert did_explode and x == ast.literal_eval("[[[[0,9],2],3],4]")
    
    x, did_explode = explode(ast.literal_eval("[7,[6,[5,[4,[3,2]]]]]"))
    assert did_explode and x == ast.literal_eval("[7,[6,[5,[7,0]]]]")

    x, did_explode = explode(ast.literal_eval("[[6,[5,[4,[3,2]]]],1]"))
    
    assert did_explode and x == ast.literal_eval("[[6,[5,[7,0]]],3]")
    
    x, did_explode = explode(ast.literal_eval("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"))
    assert did_explode and x == ast.literal_eval("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")

    x, did_explode = explode(ast.literal_eval("[[3,[2,[8,0]]],[9,[5,[7,0]]]]"))
    assert not did_explode and x == ast.literal_eval("[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
    
    x, did_split = split(ast.literal_eval("10"))
    assert did_split and x == ast.literal_eval("[5,5]")

    x, did_split = split(ast.literal_eval("11"))
    assert did_split and x == ast.literal_eval("[5,6]")
    
    x = add(ast.literal_eval("[[[[4,3],4],4],[7,[[8,4],9]]]"), ast.literal_eval("[1,1]"))
    assert x == ast.literal_eval("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
    
    x, did_explode = explode(x)
    assert did_explode and x == ast.literal_eval("[[[[0,7],4],[7,[[8,4],9]]],[1,1]]")
    
    x, did_explode = explode(x)
    assert did_explode and x == ast.literal_eval("[[[[0,7],4],[15,[0,13]]],[1,1]]")
    
    x, did_split = split(x)
    assert did_split and x == ast.literal_eval("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
    
    x, did_split = split(x)
    assert did_split and x == ast.literal_eval("[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]")
    
    x, did_explode = explode(x)
    assert did_explode and x == ast.literal_eval("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")

    test1 = """[1,1]\n[2,2]\n[3,3]\n[4,4]""".split("\n")
    assert add_lines(test1) == ast.literal_eval("[[[[1,1],[2,2]],[3,3]],[4,4]]")

    test2 = """[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]""".split("\n")
    assert add_lines(test2) == ast.literal_eval("[[[[3,0],[5,3]],[4,4]],[5,5]]")

    test3 = """[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]\n[6,6]""".split("\n")
    assert add_lines(test3) == ast.literal_eval("[[[[5,0],[7,4]],[5,5]],[6,6]]")
    
    test4 = [
      '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
      '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
      '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
      '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
      '[7,[5,[[3,8],[1,4]]]]',
      '[[2,[2,2]],[8,[8,1]]]',
      '[2,9]',
      '[1,[[[9,3],9],[[9,0],[0,7]]]]',
      '[[[5,[7,4]] ,7],1]',
      '[[[[4,2],2],6],[8,7]]',
    ]
    assert add_lines(test4) == ast.literal_eval("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")

    x = add_lines(["[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]", "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"])
    assert x == ast.literal_eval("[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")

    x = add_lines(["[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]", "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"])
    assert x == ast.literal_eval("[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")

    x = add_lines(
        ["[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]", "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]"])
    assert x == ast.literal_eval("[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]")

    x = add_lines(["[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]",
                   "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]"])
    assert x == ast.literal_eval("[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]")

    x = add_lines(["[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]", "[7,[5,[[3,8],[1,4]]]]"])
    assert x == ast.literal_eval("[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]")

    x = add_lines(["[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]", "[[2,[2,2]],[8,[8,1]]]"])
    assert x == ast.literal_eval("[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]")

    x = add_lines(["[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]", "[2,9]"])
    assert x == ast.literal_eval("[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]")

    x = add_lines(["[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]", "[1,[[[9,3],9],[[9,0],[0,7]]]]"])
    assert x == ast.literal_eval("[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]")

    x = add_lines(["[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]", "[[[5,[7,4]],7],1]"])
    assert x == ast.literal_eval("[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]")

    x = add_lines(["[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]", "[[[[4,2],2],6],[8,7]]"])
    assert x == ast.literal_eval("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")

    assert magnitude(ast.literal_eval("[9,1]")) == 29
    assert magnitude(ast.literal_eval("[1,9]")) == 21
    assert magnitude(ast.literal_eval("[[9,1],[1,9]]")) == 129
    assert magnitude(ast.literal_eval("[[1,2],[[3,4],5]]")) == 143
    assert magnitude(ast.literal_eval("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")) == 1384
    assert magnitude(ast.literal_eval("[[[[1,1],[2,2]],[3,3]],[4,4]]")) == 445
    assert magnitude(ast.literal_eval("[[[[3,0],[5,3]],[4,4]],[5,5]]")) == 791
    assert magnitude(ast.literal_eval("[[[[5,0],[7,4]],[5,5]],[6,6]]")) == 1137
    assert magnitude(ast.literal_eval("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")) == 3488

    test5 = [
      '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
      '[[[5,[2,8]],4],[5,[[9,9],0]]]',
      '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
      '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
      '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
      '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
      '[[[[5,4],[7,7]],8],[[8,3],8]]',
      '[[9,3],[[9,9],[6,[4,9]]]]',
      '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
      '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]',
    ]
    x = add_lines(test5)
    assert x == ast.literal_eval("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]")
    assert magnitude(x) == 4140

run_tests()

print(magnitude(add_lines(lines)))

# lines = [
#   '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
#   '[[[5,[2,8]],4],[5,[[9,9],0]]]',
#   '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
#   '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
#   '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
#   '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
#   '[[[[5,4],[7,7]],8],[[8,3],8]]',
#   '[[9,3],[[9,9],[6,[4,9]]]]',
#   '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
#   '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]',
# ]

magnitudes = []
for line1 in lines:
  for line2 in lines:
    m = magnitude(add_lines([line1, line2]))
    magnitudes.append(m)
print(max(magnitudes))
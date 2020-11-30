#!/usr/bin/env python3

input_txt = '704321'

def print_state(leaderboard, pos_elf_1, pos_elf_2):
  result = []  
  for idx, c in enumerate(leaderboard):
    if idx == pos_elf_1:
      cc = "({})".format(c)
    elif idx == pos_elf_2:
      cc = "[{}]".format(c)
    else:
      cc = " {} ".format(c)
    result.append(cc)
  result = "".join(result)
  print(result)
  return result

leaderboard = [3, 7]
pos_elf_1 = 0
pos_elf_2 = 1

def next_state(leaderboard, pos_elf_1, pos_elf_2):
  leaderboard = add_recipes(leaderboard, pos_elf_1, pos_elf_2)
  pos_elf_1, pos_elf_2 = move_elves(leaderboard, pos_elf_1, pos_elf_2)
  return leaderboard, pos_elf_1, pos_elf_2

def add_recipes(leaderboard, pos_elf_1, pos_elf_2):
  score_elf_1 = leaderboard[pos_elf_1]
  score_elf_2 = leaderboard[pos_elf_2]
  score = score_elf_1 + score_elf_2
  for d in str(score):
    leaderboard.append(int(d))
  return leaderboard

def move_elves(leaderboard, pos_elf_1, pos_elf_2):
  n_moves_elf_1 = leaderboard[pos_elf_1] + 1
  n_moves_elf_2 = leaderboard[pos_elf_2] + 1
  pos_elf_1 = (pos_elf_1 + n_moves_elf_1) % len(leaderboard)
  pos_elf_2 = (pos_elf_2 + n_moves_elf_2) % len(leaderboard)
  return pos_elf_1, pos_elf_2


# print_state(leaderboard, pos_elf_1, pos_elf_2)
# print('pos_elf_1={} pos_elf_2={}'.format(pos_elf_1, pos_elf_2))

N_RECIPES = 10
AFTER_N = 5
# AFTER_N = 18
# AFTER_N = 2018
# AFTER_N = int(input_txt)

for i in range(N_RECIPES + AFTER_N):
  leaderboard, pos_elf_1, pos_elf_2 = next_state(leaderboard, pos_elf_1, pos_elf_2)
  # print_state(leaderboard, pos_elf_1, pos_elf_2)
  

print('Part 1 answer:', "".join([str(d) for d in leaderboard[AFTER_N:AFTER_N + N_RECIPES]]))

leaderboard = '37'
pos_elf_1 = 0
pos_elf_2 = 1

def next_state(leaderboard, pos_elf_1, pos_elf_2):
  leaderboard = add_recipes(leaderboard, pos_elf_1, pos_elf_2)
  pos_elf_1, pos_elf_2 = move_elves(leaderboard, pos_elf_1, pos_elf_2)
  return leaderboard, pos_elf_1, pos_elf_2

def add_recipes(leaderboard, pos_elf_1, pos_elf_2):
  score_elf_1 = int(leaderboard[pos_elf_1])
  score_elf_2 = int(leaderboard[pos_elf_2])
  score = score_elf_1 + score_elf_2
  for d in str(score):
    leaderboard += d
  return leaderboard

def move_elves(leaderboard, pos_elf_1, pos_elf_2):
  n_moves_elf_1 = int(leaderboard[pos_elf_1]) + 1
  n_moves_elf_2 = int(leaderboard[pos_elf_2]) + 1
  pos_elf_1 = (pos_elf_1 + n_moves_elf_1) % len(leaderboard)
  pos_elf_2 = (pos_elf_2 + n_moves_elf_2) % len(leaderboard)
  return pos_elf_1, pos_elf_2

target = input_txt
# target = '51589'
# target = '01245'
# target = '92510'
# target = '59414'

target_len = len(target)

elf1 = 0
elf2 = 1

while target not in leaderboard[-target_len:]:
    leaderboard += str(int(leaderboard[elf1]) + int(leaderboard[elf2]))
    elf1 = (elf1 + int(leaderboard[elf1]) + 1) % len(leaderboard)
    elf2 = (elf2 + int(leaderboard[elf2]) + 1) % len(leaderboard)

print('Part 2 answer:', leaderboard.index(target))

#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]

# input_txt = [
#     'Disc #1 has 5 positions; at time=0, it is at position 4.',
#     'Disc #2 has 2 positions; at time=0, it is at position 1.'
# ]

# print(input_txt)

# class Disc():
#     def __init__(self, def_str):
#         pt1, pt2 = def_str.split(';')
#         _, id, __, n_pos, ___ = pt1.strip().split(' ')
#         self.id = id
#         self.n_pos = int(n_pos)

#         s_pos = pt2.strip().split(' ')[-1][:-1]
#         self.s_pos = int(s_pos)
#         self.c_pos = int(s_pos)
        
#         time = pt2.strip().split(' ')[1]
#         self.time = int(time.split('=')[-1][:-1])
#         self.ticks = int(time.split('=')[-1][:-1])

#     def __str__(self):
#         return self.id + ': n_pos=' + str(self.n_pos) + ', s_pos=' + str(self.s_pos) + ', c_pos=' + str(self.c_pos) + ', time=' + str(self.time) + ', ticks=' + str(self.ticks)
    
#     def tick_forward(self):
#         self.c_pos = (self.c_pos + 1) % self.n_pos

#     def state_at(self, T=0):
#         disc_n = int(self.id[1:])
#         self.ticks = T + disc_n

#         for i in range(self.ticks):
#             self.tick_forward()

#         self.time = T


# i = 0
# while True:
#     slot_count = 0

#     for line in input_txt:
#         d = Disc(line)
#         d.state_at(i)
#         slot_count += d.c_pos
#     #     print('T=', i, d)

#     # print('\n')

#     if slot_count == 0:
#         break    
    
#     i += 1

# def d1(t=0):
#     return (t + 4) % 5

# def d2(t=0):
#     return (t + 1) % 2

# T = 0
# while True:
#     slots = [d1(T + 1), d2(T + 2)]
#     if sum(slots) == 0:
#         break

#     T += 1

def d1(t=0):
    return (t + 11) % 13 == 0

def d2(t=0):
    return (t + 0) % 5 == 0

def d3(t=0):
    return (t + 11) % 17 == 0

def d4(t=0):
    return (t + 0) % 3 == 0

def d5(t=0):
    return (t + 2) % 7 == 0

def d6(t=0):
    return (t + 17) % 19 == 0

T = 0
while True:
    if d1(T+1) and d2(T+2) and d3(T+3) and d4(T+4) and d5(T+5) and d6(T+6):
        break

    T += 1


print("Part 1 answer:", T)

def d7(t=0):
    return (t + 0) % 11 == 0

T = 0
while True:
    if d1(T+1) and d2(T+2) and d3(T+3) and d4(T+4) and d5(T+5) and d6(T+6) and d7(T+7):
        break

    T += 1

print("Part 2 answer:", T)

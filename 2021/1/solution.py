#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]
measurements = [int(x) for x in lines]

# measurements = [
#   199,
#   200,
#   208,
#   210,
#   200,
#   207,
#   240,
#   269,
#   260,
#   263
# ]

increases = 0

for idx, measurement in enumerate(measurements):
  if idx == 0:
    continue
  if measurement > measurements[idx-1]:
    increases += 1

print(increases)

window_size = 3

sum_measurements = []
for i in range(len(measurements) - window_size + 1):
  sum_measurements.append(sum(measurements[i: i + window_size]))

increases = 0

for idx, measurement in enumerate(sum_measurements):
  if idx == 0:
    continue
  if measurement > sum_measurements[idx-1]:
    increases += 1

print(increases)
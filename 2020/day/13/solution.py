#!/usr/bin/env python3

import os
from functools import reduce

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '939',
#   '7,13,x,x,59,x,31,19',
# ]

earliest_bus = None
earliest_ts = int(lines[0])
buses = [int(x) for x in filter(lambda x: x != 'x', lines[1].split(','))]

# print(earliest_bus, earliest_ts, buses)

bus_schedules = {}

for bus in buses:
  schedule = range(0, earliest_ts + bus, bus)
  if earliest_ts in schedule:
    earliest_bus = bus
    break
  
  closest_for_schedule = min(schedule, key=lambda x:abs(x-earliest_ts))
  bus_schedules[bus] = closest_for_schedule

earliest_bus = min(filter(lambda x: x[1] >= earliest_ts, bus_schedules.items()), key=lambda x: x[1])

print('Part 1:', earliest_bus[0] * (earliest_bus[1] - earliest_ts))


# lines = [
#   '939',
#   '17,x,13,19',
# ]
# lines = [
#   '939',
#   '67,7,59,61',
# ]
# lines = [
#   '939',
#   '67,x,7,59,61',
# ]
# lines = [
#   '939',
#   '67,7,x,59,61',
# ]
# lines = [
#   '939',
#   '1789,37,47,1889',
# ]

buses = [0 if x == 'x' else int(x) for x in lines[1].split(',')]


def sync(buses):
    indices = [i for i, bus in enumerate(buses) if bus]
    diff = indices[-1] - indices[0]
    prod = reduce(lambda a, b: a * b, filter(None, buses))
    return sum((diff - i) * pow(prod // n, n - 2, n) * prod // n
               for i, n in enumerate(buses) if n) % prod - diff

print('Part 2:', sync(buses))
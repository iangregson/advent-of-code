#!/usr/bin/env python3

import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]

# input_txt = [
#   '[1518-11-01 00:00] Guard #10 begins shift',
#   '[1518-11-01 00:05] falls asleep',
#   '[1518-11-01 00:25] wakes up',
#   '[1518-11-01 00:30] falls asleep',
#   '[1518-11-01 00:55] wakes up',
#   '[1518-11-01 23:58] Guard #99 begins shift',
#   '[1518-11-02 00:40] falls asleep',
#   '[1518-11-02 00:50] wakes up',
#   '[1518-11-03 00:05] Guard #10 begins shift',
#   '[1518-11-03 00:24] falls asleep',
#   '[1518-11-03 00:29] wakes up',
#   '[1518-11-04 00:02] Guard #99 begins shift',
#   '[1518-11-04 00:36] falls asleep',
#   '[1518-11-04 00:46] wakes up',
#   '[1518-11-05 00:03] Guard #99 begins shift',
#   '[1518-11-05 00:45] falls asleep',
#   '[1518-11-05 00:55] wakes up'
# ]

input_txt = sorted(input_txt)

class Line():
  def __init__(self, line, guard_id=None):
    self.line = line
    
    ts, rest = line.split('] ')
    self.ts = ts[1:]
    
    self.action = None
    if 'wakes' in rest:
      self.state = 'AWAKE'
    elif 'asleep' in rest:
      self.state = 'ASLEEP'
    elif 'shift' in rest:
      self.state = 'START SHIFT'  

    self.guard_id = guard_id
    if '#' in rest:
      self.guard_id = rest.split(' ')[1]

  def __str__(self):
    s = "{} {}".format(self.ts, self.state)
    if self.guard_id is not None:
      s += " " + self.guard_id
    return s

  def is_shift_start(self):
    return self.state == 'START SHIFT'
  
  def is_awake(self):
    return self.state == 'AWAKE'

  def is_asleep(self):
    return self.state == 'ASLEEP'

  def parse_ts(self):
    date, time = self.ts.split(' ')
    h, m = time.split(':')
    return (date, int(h), int(m))

class Guard():
  def __init__(self, id):
    self.id = id
    self.int_id = int(id[1:])
    self.data = []

  def append(self, d):
    self.data.append(d)

  def __str__(self):
    return "\n".join([str(s) for s in self.data])

  def time_asleep(self):
    time_asleep = 0
    mm = None
    for line in self.data:
      d, h, m = line.parse_ts()
      if line.is_shift_start():
        continue
      if line.is_asleep():
        mm = m
      if line.is_awake():
        time_asleep += m - mm
    return time_asleep

  def common_sleep_minute(self):
    # print('\ncalled Guard::common_sleep_minute\n')
    sleeps = []
    mm = None
    # print('self.data', [str(s) for s in self.data])
    for line in self.data:
      d, h, m = line.parse_ts()
      if line.is_shift_start():
        continue
      if line.is_asleep():
        mm = m
      if line.is_awake():
        sleeps.append((mm, m))

    sleep_minutes = defaultdict(int)
    for sleep in sleeps:
      f, t = sleep
      for i in range(f, t):
        sleep_minutes[i] += 1

    # print('sleep_minutes', sleep_minutes.items())
    sorted_sleep_mintes = sorted(sleep_minutes.items(), key=lambda x: x[1])
    # print('sorted_sleep_minutes', sorted_sleep_mintes)

    if not len(sorted_sleep_mintes):
      return (0, 0)

    return sorted_sleep_mintes.pop()
 
def strategy_1(guards):
  total_sleep_times = defaultdict(int)
  for g in guards.values():
    total_sleep_times[g.id] = g.time_asleep()

  sorted_total_sleep_times = sorted(total_sleep_times.items(), key=lambda x: x[1])
  longest_sleep_guard = sorted_total_sleep_times.pop()[0]

  return guards[longest_sleep_guard].int_id * guards[longest_sleep_guard].common_sleep_minute()[0]
  
def strategy_2(guards):
  common_sleep_minutes = []
  for g in guards.values():
    minute, freq = g.common_sleep_minute()
    common_sleep_minutes.append((g.int_id, minute, freq))

  chosen_guard = sorted(common_sleep_minutes, key=lambda x: x[2]).pop()
  id, minute, freq = chosen_guard
  return id * minute

guards = {}
current_guard_id = None
for line in input_txt:
  l = Line(line, current_guard_id)

  if l.is_shift_start():
    current_guard_id = l.guard_id

  if l.guard_id not in guards:
    g = Guard(l.guard_id)
    guards[l.guard_id] = g
  
  guards[l.guard_id].append(l)

print("Part 1 answer:", strategy_1(guards))
print("Part 2 answer:", strategy_2(guards))
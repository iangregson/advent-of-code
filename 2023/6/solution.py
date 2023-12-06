from collections import defaultdict
from operator import mul
from functools import reduce
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
text = file.read_text()

times, distances = text.split('\n')
times = [int(x) for x in times.split(': ')[1].split()]
distances = [int(x) for x in distances.split(': ')[1].split()]

n_races = len(times)
UNIT_MM_S = 1

def hold_to_distance(hold: int, race_time: int) -> int:
  v = hold * UNIT_MM_S
  t = race_time - hold
  d = v * t
  return d

races = defaultdict(list)
for race in range(n_races):
  time = times[race]
  distance = distances[race]
  for hold in range(1, time):
    d = hold_to_distance(hold, time)
    if d > distance:
      races[race].append(hold)
    
# print(races)

error_margin = reduce(mul, [len(race) for race in races.values()])
print(error_margin)


# Part 2 ------------------------------------------------

times, distances = text.split('\n')
time = int("".join(times.split(':')[1].split()))
distance = int("".join(distances.split(':')[1].split()))

first_hold_beat_d = 0
for hold in range(1, time//2):
  d = hold_to_distance(hold, time)
  if d > distance:
    first_hold_beat_d = hold
    break

max_hold_beat_d = time - first_hold_beat_d
print(max_hold_beat_d - (first_hold_beat_d-1))


from dataclasses import dataclass
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
text = file.read_text()

@dataclass
class Mapping():
  type: str
  dst: int
  src: int
  len: int

lines = text.split('\n\n')
seeds, mappings = lines[0], lines[1:]
seeds = [int(s) for s in seeds.split(': ')[1].split(' ')]


almanac = {}
for m in mappings:
  type, mappings = m.split('\n')[0], m.split('\n')[1:]
  type = type.replace(' map:', '')
  mappings = [tuple(map(int, mapping.split())) for mapping in mappings]
  mappings = [Mapping(type, *mapping) for mapping in mappings] 
  almanac[type] = mappings


locations = []

def map_seed(seed: int, frm: str, to: str, almanac: dict[str, Mapping]) -> int:
  M = almanac[f"{frm}-to-{to}"]
  for m in M:
    if seed >= m.src and seed < m.src + m.len:
      offset = seed - m.src
      return m.dst + offset
  return seed

locations = []
for seed in seeds:
  for mapping_type in almanac:
    frm, to = mapping_type.split('-to-')
    seed = map_seed(seed, frm, to, almanac)
  locations.append(seed)

# print(locations)
print(min(locations))
  

# Part 2 ---------------------------------------------

seed_range = (0,0)
sorted_almanac = {}

seed_ranges = []
for i in range(0, len(seeds) - 1, 2):
  seed_ranges = seed_ranges + [(seeds[i], seeds[i+1])]

for mtype in almanac:
  mappings = almanac[mtype]
  sorted_almanac[mtype] = sorted(mappings, key=lambda m: m.dst)

def map_seed_range(seed_ranges: list[tuple[int]], frm: str, to: str, almanac: dict[str, Mapping]) -> tuple[int]:
  M = almanac[f"{frm}-to-{to}"]

  mapped = []
  for m in M:
    not_mapped = []
    src_end = m.src + m.len
    while seed_ranges:
      start, end = seed_ranges.pop()
      before = (start, min(end, m.src))
      intersection = (max(start, m.src), min(end, src_end))
      after = (max(start, src_end), end)

      if before[1] > before[0]:
        not_mapped.append(before)
      if intersection[1] > intersection[0]:
        mapped.append((intersection[0] - m.src+m.dst, intersection[1] - m.src+m.dst))
      if after[1] > after[0]:
        not_mapped.append(after)

    seed_ranges = not_mapped
  
  return mapped + seed_ranges

location_ranges = []
for seed_range in seed_ranges:
  seed_range = [(seed_range[0], seed_range[0] + seed_range[1])]
  for mapping_type in sorted_almanac:
    frm, to = mapping_type.split('-to-')
    seed_range = map_seed_range(seed_range, frm, to, sorted_almanac)
    # print(mapping_type, seed_range)
  location_ranges.append(min(seed_range))

print(min(location_ranges)[0])
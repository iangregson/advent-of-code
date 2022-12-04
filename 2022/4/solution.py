from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

count_superset = 0
count_intersection = 0
for line in text:
  a, b = line.split(',')
  a, b = tuple(map(int, a.split('-'))), tuple(map(int, b.split('-')))
  a, b = list(range(a[0], a[1]+1)), list(range(b[0], b[1]+1))

  if len(set(a).intersection(set(b))) == len(a):
    count_superset += 1
  elif len(set(b).intersection(set(a))) == len(b):
    count_superset += 1

  if len(set(a).intersection(set(b))) > 0:
    count_intersection += 1
  elif len(set(b).intersection(set(a))) > 0:
    count_intersection += 1

print("Part 1:", count_superset)
print("Part 2:", count_intersection)

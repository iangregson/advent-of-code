from functools import cache
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example2.txt'
text = file.read_text()


def hash(s: str) -> int:
  cv = 0
  for c in s:
    ac = ord(c)   # Determine the ASCII code for the current character of the string.
    cv += ac      # Increase the current value by the ASCII code you just determined.
    cv = cv * 17  # Set the current value to itself multiplied by 17.
    cv = cv % 256 # Set the current value to the remainder of dividing itself by 256.

  return cv

# print(hash('HASH'))

seq = text
parts = seq.split(',')

s = 0
for part in parts:
  h = hash(part)
  # print(h)
  s += h

print(s)

# Part 2 -----------------------------------------

boxes = [[] for _ in range(256)]
focal_map = {}

seq = text
parts = seq.split(',')

for part in parts:
  if part.endswith('-'):
    p = part[:-1]
    box_n = hash(p)
    for i in range(len(boxes[box_n])):
      box = boxes[box_n][i]
      if box[0] == p:
        boxes[box_n].pop(i)
        break
  else:
    p, n = part.split('=')
    box_n = hash(p)
    focal_map[p] = int(n)
    n = int(n)

    found = False
    for i in range(len(boxes[box_n])):
      box = boxes[box_n][i]
      if box[0] == p:
        boxes[box_n].pop(i)
        boxes[box_n].insert(i, (p,n))
        found = True
        break

    if not found:
      boxes[box_n].append((p,n))
  
  # print(part)
  # for idx, box in enumerate(boxes):
  #   if len(box) > 0:
  #     print(idx, box)
  # print()

def focus_power(lens: tuple[str, int], box_n: int, box: list[tuple[str, int]]) -> int:
  fp = 1 + box_n            # One plus the box number of the lens in question.
  fp *= box.index(lens) + 1 # The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
  fp *= lens[1]             # The focal length of the lens.
  return fp


ans = 0
for box_n, box in enumerate(boxes):
  if len(box) == 0:
    continue

  for lens in box:
    fp = focus_power(lens, box_n, box)
    ans += fp

print(ans)
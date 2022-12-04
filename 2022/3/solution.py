from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

def char_to_priority(char):
  if char.isupper():
    return ord(char) - 38
  else:
    return ord(char) - 96

common_items = []
for line in text:
  n = len(line)
  p = n // 2
  a, b = line[:p], line[p:]
  common_item = set(a).intersection(set(b))
  common_items.append(list(common_item)[0])

print("Part 1", sum(map(char_to_priority, common_items)))


common_items = []
n = len(text)
for i in range(3, n+1, 3):
  a, b, c = text[i-3], text[i-2], text[i-1]
  common_item = set(a).intersection(set(b))
  common_item = common_item.intersection(set(c))
  common_items.append(list(common_item)[0])

print("Part 2", sum(map(char_to_priority, common_items)))
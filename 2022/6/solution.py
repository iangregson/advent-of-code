from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
# file = Path(__file__).parent / 'test_input_2.txt'
# file = Path(__file__).parent / 'test_input_3.txt'
# file = Path(__file__).parent / 'test_input_4.txt'
# file = Path(__file__).parent / 'test_input_5.txt'
text = file.read_text()

def has_unique_chars(chars):
  return len(set(chars)) == len(chars)

n = len(text)
for i in range(4, n):
  window = text[i-4:i]
  if has_unique_chars(window):
    print("Part 1:", i)
    break

for i in range(14, n):
  window = text[i-14:i]
  if has_unique_chars(window):
    print("Part 2:", i)
    break

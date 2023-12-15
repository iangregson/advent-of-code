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

print(hash('HASH'))

seq = text
parts = seq.split(',')

s = 0
for part in parts:
  h = hash(part)
  # print(h)
  s += h

print(s)


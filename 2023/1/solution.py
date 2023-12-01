import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
text = file.read_text()

# text = """
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# """

lines = text.strip().split('\n')
sum = 0
for line in lines:
  digits = []
  for char in line:
    if char.isnumeric():
      digits.append(int(char))
  sum += int(f"{digits[0]}{digits[-1]}")
    
print(sum)

# Part 2 ---------------------------------------------

# text = """
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# """

lines = text.strip().split('\n')

replacements = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

sum = 0
for line in lines:
  parts = []
  i, j, n = 0, 0, len(line)
  while i < n:
    a = line[i]
    if a.isnumeric():
      parts.append(a)
      i += 1
    else:
      part = ""
      j = i
      if j == n - 1:
        break
      while j < n:
        b = line[j]
        j += 1
        if b.isnumeric():
          break
        part += b
      parts.append(part)
      i = j - 1

  numbers = []
  for part in parts:
    if part.isnumeric():
      numbers.append(part)
    else:
      possible_numbers = []
      for replacement in replacements:
        idx = 0
        while idx < len(part):
          idx = part.find(replacement, idx)
          if idx == -1:
            break
          possible_numbers.append((idx, replacements[replacement]))
          idx += len(replacement)
      possible_numbers = sorted(possible_numbers)
      numbers += [b for _, b in possible_numbers]

  # print(line)
  # print(numbers)
  sum += int(f"{numbers[0]}{numbers[-1]}")

print(sum)

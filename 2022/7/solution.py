from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

fs = {}
cd = []
while text:
  line = text.pop(0)

  if line.startswith('$ cd'):
    _, __, d = line.split()
    if d == '..':
      cd.pop()
    else:
      cd.append(d)
  elif line.startswith('$ ls'):
    outputs = [] 
    while text and not text[0].startswith('$'):
      outputs.append(text.pop(0))  

    if len(cd) > 1:
      pwd = "/" + "/".join(cd[1:])
    else:
      pwd = cd[0]
    
    fs[pwd] = outputs

def dir_size(dir_name, fs):
  size = 0
  dir_contents = fs[dir_name]
  for item in dir_contents:
    a, b = item.split()
    if a == 'dir':
      if dir_name.endswith('/'):
        pwd = dir_name + b
      else:
        pwd = f"{dir_name}/{b}"

      size += dir_size(pwd, fs)
    else:
      size += int(a)
  
  return size

MAX_SIZE = 100000
print("Part 1:", sum([dir_size(d, fs) for d in fs if dir_size(d, fs) <= MAX_SIZE]))

TOTAL_DISK = 70000000
UPDATE_SIZE = 30000000
space_req = UPDATE_SIZE - (TOTAL_DISK - dir_size('/', fs))
print("Part 2:", min([dir_size(d, fs) for d in fs if dir_size(d, fs) >= space_req]))

import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
text = file.read_text()

def extrapolate(line: list[int]):
  nls = [line[:]]
  s = 0
  while True:
    l = nls[s]
    nl = []
    for i in range(len(l)-1):
      j = i + 1
      a,b = l[i], l[j]
      nl.append(b-a)
    
    nls.append(nl)
    if all(x==0 for x in nl):
      break
    
    s += 1

  # for l in nls:
  #     print(l)

  for j in range(len(nls)-1,0,-1):
      i = j - 1
      # print(i,j)
      m,l = nls[j], nls[i]
      # print(m,l)
      a,b = m[-1], l[-1]
      c = b + a
      nls[i].append(c)
      # print(nls[i])

  return nls[0][-1]

lines = [[int(x) for x in line.split(' ')] for line in text.splitlines()]

s = 0
for line in lines:
  #  print('\n')
   a = extrapolate(line)
  #  print(a)
   s += a

# print('\n')
print(s)

# Part 2 ----------------------------------------------

def extrapolate(line: list[int]):
  nls = [line[:]]
  s = 0
  while True:
    l = nls[s]
    nl = []
    for i in range(len(l)-1):
      j = i + 1
      a,b = l[i], l[j]
      nl.append(b-a)
    
    nls.append(nl)
    if all(x==0 for x in nl):
      break
    s += 1

  # for l in nls:
  #     print(l)

  for j in range(len(nls)-1,0,-1):
      i = j - 1
      # print(i,j)
      m,l = nls[j], nls[i]
      # print(m,l)
      a,b = m[0], l[0]
      c = b - a
      nls[i].insert(0, c)
      # print(nls[i])

  return nls[0][0]

s = 0
for line in lines:
  # print('\n')
  a = extrapolate(line)
  # print(a)
  s += a

# print('\n')
print(s)


# recursive
def extrapolate_recursive(line: list[int], mod=(-1,1)):
  nl = []
  for i in range(len(line)-1):
    nl.append(line[i+1] - line[i])
  
  if all(x == 0 for x in nl):
    return line[mod[0]]
  else:
    return line[mod[0]] + (mod[1]*extrapolate_recursive(nl, mod))

s = 0
for line in lines:
  # print('\n')
  a = extrapolate_recursive(line)
  # print(a)
  s += a
# print('\n')
print(s)

s = 0
for line in lines:
  # print('\n')
  a = extrapolate_recursive(line, (0,-1))
  # print(a)
  s += a
# print('\n')
print(s)
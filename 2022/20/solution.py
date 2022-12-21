from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

class File():
  def __init__(self, buffer = []) -> None:
    self._buffer = list(enumerate(buffer))

  def __len__(self):
    return len(self._buffer)

  def digest(self):
    return [i[1] for i in self._buffer]

  def __repr__(self) -> str:
     return f"{self}"

  def __str__(self) -> str:
     return ", ".join([str(x) for x in self.digest()])

  @staticmethod
  def from_text(text, key = 1):
    return File([int(line) * key for line in text])

  def __getitem__(self, idx):
    return self._buffer[idx]

  def popleft(self):
    return self._buffer.pop(0)

  def append(self, val):
    return self._buffer.append(val)

  def mix(self):
    for i in range(len(self)):
      while self[0][0] != i:
        self.append(self.popleft())
      
      k,v = self.popleft()
      for _ in range(v % len(self)):
        self.append(self.popleft())
      
      self.append((k,v))
  
  def grove_coordinates(self, target_value = 0):
    idx = None
    for i, val in enumerate(self.digest()):
      if val == target_value:
        idx = i
        break

    digest = self.digest()
    n = len(digest)
    
    x,y,z = digest[(idx+1000)%n], digest[(idx+2000)%n], digest[(idx+3000)%n]
    return x, y, z

f = File.from_text(text)
f.mix()
print("Part 1:", sum(f.grove_coordinates()))

f = File.from_text(text, key=811589153)
for _ in range(10):
  f.mix()
print("Part 2:", sum(f.grove_coordinates()))

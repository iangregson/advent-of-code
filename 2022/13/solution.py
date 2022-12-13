from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text()

class Packet():
  def __init__(self, p) -> None:
    if isinstance(p, int):
      self.p = [p]
    else:
      self.p = p

    if not isinstance(self.p, list):
      raise Exception("packet must be a list")

  def __str__(self) -> str:
    return f"{self.p}"

  def __getitem__(self, key):
    try:
      result = self.p[key]
    except IndexError:
      result = None
    return result

  def __eq__(self, other):
    return self.p == other.p

  def __gt__(self, other):
    return self != other and not self < other

  def __lt__(self, other):
    lidx, ridx = 0,0
    lptr, rptr = self[0], other[0]

    while True:
      lptr, rptr = self[lidx], other[ridx]
      if lptr is not None and rptr is None:
        return False
      
      if lptr is None or rptr is None:
        break

      # print(f"Compare {lptr} vs {rptr}")

      if isinstance(lptr, int) and isinstance(rptr, int):
        if lptr == rptr:
          lidx, ridx = lidx + 1, ridx + 1
          continue
        if lptr < rptr:
          return True
        if lptr > rptr:
          return False
      
      if isinstance(lptr, list) or isinstance(rptr, list):
        if Packet(lptr) == Packet(rptr):
          lidx, ridx = lidx + 1, ridx + 1
          continue
        elif Packet(lptr) < Packet(rptr):
          return True
        elif Packet(lptr) > Packet(rptr):
          return False

    return True

class Pair():
  def __init__(self, pair) -> None:
    self.pair = pair

    if not isinstance(self.pair, list):
      raise Exception("pair must be a list")

  def __str__(self) -> str:
    return "\n".join([f"{self.left}", f"{self.right}"])

  @property
  def left(self):
    return Packet(self.pair[0])

  @property
  def right(self):
    return Packet(self.pair[1])

  @property
  def correct_order(self):
    return self.left < self.right


pairs = [list(map(eval, pair.split('\n'))) for pair in text.split('\n\n')]
pairs = [Pair(p) for p in pairs]

correct_idxs = []
for i in range(1, len(pairs) + 1):
  pair = pairs[i-1]
  if pair.correct_order:
    correct_idxs.append(i)

print("Part 1:", sum(correct_idxs))

divider_1 = Packet([[2]])
divider_2 = Packet([[6]])
packets = [divider_1, divider_2]
for pair in pairs:
  packets.append(pair.left)
  packets.append(pair.right)
packets.sort()
divider_1_idx = packets.index(divider_1) + 1 
divider_2_idx = packets.index(divider_2) + 1

print("Part 2:", divider_1_idx * divider_2_idx)


from pathlib import Path
import random

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

class Expr():
  def __init__(self, name, expr = []) -> None:
    self.name = name
    self.type = 'expr'
    self._expr = tuple(expr)
    
    try:
      value = int(expr[0])
      self.type = 'int'
    except:
      pass

  def __repr__(self) -> str:
    if self.type == 'int':
      return f"{self._expr[0]}"
      
    a, op, b = self._expr
    return f"{a} {op} {b}"

  def __str__(self) -> str:
    if self.type == 'int':
      return f"{self.name}: {self._expr[0]}"
      
    a, op, b = self._expr
    return f"{self.name}: {a} {op} {b}"

  def eval(self, scope = {}):
    if self.type == 'int':
      return int(self._expr[0])
      
    a, op, b = self._expr

    a = scope[a].eval(scope)
    b = scope[b].eval(scope)

    return int(eval(f"{a} {op} {b}"))

  def set_val(self, val):
    self.type = 'int'
    self._expr = tuple([val])

  def equality_score(self, scope):
    a, _, b = self._expr

    a = scope[a].eval(scope)
    b = scope[b].eval(scope)

    return b - a

  @staticmethod
  def from_text(text):
    name, expr = text.split(': ')
    expr = expr.split()
    return Expr(name, expr)


expressions = {}

for line in text:
  e = Expr.from_text(line)
  expressions[e.name] = e

print("Part 1:", expressions['root'].eval(expressions))

print(expressions['root']._expr)
# print(expressions['fglq'].eval(expressions))
# print(expressions['fzbp'].eval(expressions))
# print(expressions['fglq'].eval(expressions) - expressions['fzbp'].eval(expressions))

left,right = 0,int(1e70)
humn = None
while left < right:
  mid = (left + right) // 2
  expressions['humn'].set_val(mid)

  equality_score = expressions['root'].equality_score(expressions)
  print(left, right, mid, equality_score)
  if equality_score == 0:
    humn = mid
    break
  elif equality_score < 0:
    left = mid + 1
  else:
    right = mid - 1


print("Part 2", humn)
from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

class Expr():
  def __init__(self) -> None:
    pass

  @staticmethod
  def from_text(text):
    name, expr = text.split(': ')
    expr = expr.split()

    if len(expr) == 1:
      expr[0] = int(expr[0])

    return name, tuple(expr)
  
  @staticmethod
  def left(name, expressions):
    name, expression = expressions[name]

    if len(expression) == 1:
      return None

    a, _, __ = expression

    return a
  
  @staticmethod
  def right(name, expressions):
    name, expression = expressions[name]

    if len(expression) == 1:
      return None

    _, __, b = expression

    return b

  @staticmethod
  def evaluate(name, expressions, override=None):
    name, expression = expressions[name]

    if override is not None and name == override[0]:
      return override[1]
    
    if len(expression) == 1:
      return int(expression[0])
      
    a, op, b = expression

    a, b = Expr.evaluate(a, expressions, override=override), Expr.evaluate(b, expressions, override=override)

    if op == '+':
      return a + b
    elif op == '*':
      return a * b
    elif op == '-':
      return a - b
    elif op == '/':
      return a / b

expressions = {}

for line in text:
  name, expression = Expr.from_text(line)
  expressions[name] = (name, expression)
  

print("Part 1:", Expr.evaluate('root', expressions))

left = Expr.left('root', expressions)
right = Expr.right('root', expressions)
left_a = Expr.evaluate(left, expressions)
right_a = Expr.evaluate(right, expressions)
left_b = Expr.evaluate(left, expressions, override=('humn', 150))
right_b = Expr.evaluate(right, expressions, override=('humn', 1))


mutable_expr, target_expr = None, None
if left_a == left_b:
  target_expr = left
  mutable_expr = right
else:
  target_expr = right
  mutable_expr = left

target_score = Expr.evaluate(target_expr, expressions)

l, r = 0, int(1e15)
while l < r:
  humn = (l + r) // 2
  score = target_score - Expr.evaluate(mutable_expr, expressions, override=('humn', humn))
  if score < 0:
    l = humn
  elif score == 0:
    break
  else:
    r = humn

print("Part 2:", humn)
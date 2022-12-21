from pathlib import Path

file = Path(__file__).parent / 'input.txt'
file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

class Resource():
  def __init__(self, type, cost) -> None:
    self.type = type
    self.cost = cost

class Robot():
  def __init__(self, type, cost) -> None:
    self.type = type
    self.cost = cost

class Blueprint():
  def __init__(self, id, specs = []) -> None:
    self.id = id
    self.specs = specs

  def __str__(self) -> str:
    return f"{self.id}\n  " + "\n  ".join(self.specs)
  
  def __repr__(self) -> str:
    return f"Blueprint<id={self.id}>"

  @staticmethod
  def from_text(text):
    id_, specs = text.split(': ')
    specs = specs.split('. ')
    return Blueprint(id_, specs)

b = Blueprint.from_text(text[0])

print(b)

# This is a DAG. We've got to go through all nodes. 
# Edge cost is minutes * cost e.g. if a clay robot costs 3 ore and it takes 3
# minutes to mine that ore, the cost is 9. If we had two ore robots, the time to
# get 3 ore would only be 1.5 so the cost of that path would be 4.5 instead of 9

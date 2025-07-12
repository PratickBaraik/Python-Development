normal_set = {1, 2, 3, 4, 5}
frozen = frozenset(normal_set)

print("Normal Set:", normal_set, type(normal_set))
print("Frozen Set:", frozen, type(frozen))

normal_set.add(6)  # This will work
print("Updated Normal Set:", normal_set)

#frozen.add(6)  # This will raise an AttributeError
#print("Updated Frozen Set:", frozen)  # This line will not execute

# hashing the frozen set with this simple python class code
class Person:
  def __init__(self, name):
    self.name = name
  
  def __hash__(self):
    return hash(self.name)
  
result = Person("Hello World")
print("Person Object:", result)
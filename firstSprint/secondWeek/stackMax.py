f = open('stackMax.txt', 'r')

numberLines = int(f.readline())
commands = list(map(lambda string: string.strip().split(), f.readlines()))

class Stack:
  def __init__(self):
    self.items = list()

  def pop(self):
    if self.isEmpty():
      return None

    return self.items.pop()

  def push(self, item):
    self.items.append(int(item))

  def isEmpty(self):
    return self.items == []

  def get_max(self):
    if self.isEmpty():
      return None
    max = self.items[0]
    for item in self.items[1:]:
      if item > max:
        max = item
    
    return max

stack = Stack()

for command in commands:
  if command[0] == 'get_max':
    print(stack.get_max())

  if command[0] == 'pop':
    if stack.pop() == None:
      print('error')

  if len(command) == 2:
    stack.push(command[1])

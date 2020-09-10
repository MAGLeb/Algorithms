f = open('stackMax.txt', 'r')

numberLines = int(f.readline())
commands = list(map(lambda string: string.strip().split(), f.readlines()))

class Stack:
  def __init__(self):
    self.items = []
    self.max = None

  def pop(self):

    if self.isEmpty():
      return None

    deletedValue = self.items.pop()

    if self.isEmpty():
      self.max = None
      return deletedValue

    self.max = max(self.items)

    return deletedValue

  def push(self, item):

    if self.max == None:
      self.max = item
    elif item > self.max:
      self.max = item

    self.items.append(item)

  def isEmpty(self):
    return self.items == []

  def get_max(self):
    return self.max

stack = Stack()

for command in commands:
  
  if command[0] == 'get_max':
    print(stack.get_max())
    continue

  if command[0] == 'pop':
    if stack.pop() == None:
      print('error')
    continue

  if command[0] == 'push':
    stack.push(int(command[1]))

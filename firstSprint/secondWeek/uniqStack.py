f = open('uniqStack.txt', 'r')

numberLines = int(f.readline())
commands = list(map(lambda string: string.strip().split(), f.readlines()))

class UniqStack:
  def __init__(self):
    self.items = []

  def push(self, item):
    if item not in self.items:
      self.items.append(item)

  def size(self):
    print(len(self.items))

  def isEmpty(self):
    return self.items == []

  def pop(self):
    if self.isEmpty():
      print('error')
      return None

    self.items.pop()

  def peek(self):
    if self.isEmpty():
      print('error')
      return None
    
    print(self.items[len(self.items) - 1])

stack = UniqStack()

for command in commands:
  if command:
    if command[0] == 'push':
      stack.push(int(command[1]))

    if command[0] == 'size':
      stack.size()

    if command[0] == 'pop':
      stack.pop()

    if command[0] == 'peek':
      stack.peek()

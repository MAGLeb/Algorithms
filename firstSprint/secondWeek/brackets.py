f = open('brackets.txt', 'r')

string = f.readline()

class Stack:
  def __init__(self):
    self.items = list()
  
  def listPrint(self):
    return self.items

  def pop(self):
    if self.isEmpty():
      return None

    return self.items.pop()

  def push(self, item):
    self.items.append(item)

  def isEmpty(self):
    return self.items == []

  def peek(self):
    if self.isEmpty():
      return None
    
    return self.items[len(self.items) - 1]

stack = Stack()

for bracket in string:
  if bracket == '{' or bracket == '(' or bracket == '[':
    stack.push(bracket)

  if bracket == '}':
    if stack.peek() == '{':
      stack.pop()
    else:
      break

  if bracket == ')':
    if stack.peek() == '(':
      stack.pop()
    else:
      break

  if bracket == ']':
    if stack.peek() == '[':
      stack.pop()
    else:
      break

if stack.isEmpty():
  print(True)
else:
  print(False)
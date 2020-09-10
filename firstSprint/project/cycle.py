class Node:
  def __init__(self, next = None):
    self.next = next
  
f = open('cycle.txt', 'r')
numberline = int(f.readline())

array = []
for i in range(numberline):
  array.append(Node())

for i in range(numberline):
  line = f.readline().split()
  if line[0] == 'None':
    array[i].next = None
  else:
    array[i].next = array[int(line[0])]

head = array[0]

def checkCycle(node):

  if node == None:
    return False

  turtle = node
  rabbit = node

  while rabbit.next != None and rabbit.next.next != None:
    turtle = turtle.next
    rabbit = rabbit.next.next
    if turtle == rabbit:
      return True
      
  return False

print(checkCycle(head))


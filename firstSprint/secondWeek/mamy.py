class Node:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

  def __str__(self):
    return self.value

def insertNode(node, index, value):
    
  head = node
  new_node = Node(value)

  if index == 0:
    new_node.next = node
    return new_node

  while index - 1:
    node = node.next
    index -= 1

  next_node = node.next
  node.next = new_node
  new_node.next = next_node

  return head

def findNode(node, value):

  index = 0

  while node != None:

    if node.value == value:
      return index
    
    index += 1
    node = node.next
      

  return -1

f = open('mamy.txt', 'r')

numbers = int(f.readline())

array = []
for i in range(numbers):
  array.append(Node())

for i in range(numbers):
  line = f.readline().strip().split()

  if line[0] == 'None':
    array[numbers - 1].next = None
    array[numbers - 1].value = ' '.join(line[1:])
  else:
    array[int(line[0]) - 1].next = array[int(line[0])]
    array[int(line[0]) - 1].value = ' '.join(line[1:])


needToFind = f.readline()
head = array[0]

f.close()

print(findNode(head, needToFind))


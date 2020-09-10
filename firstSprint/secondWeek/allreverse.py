f = open('allreverse.txt', 'r')

numberLines = int(f.readline())
array = sorted(list(map(lambda item: item.rstrip().rsplit(), f.readlines())))

class Node:
  def __init__(self, value = None, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

  def __str__(self):
    return self.value

def printList(node):

  while node.next != None:
    node = node.next

  while node != None:
    print(node)
    node = node.prev

def insertNode(node, index, value):
    
  head = node
  new_node = Node(value)

  if index == 0:
    new_node.next = node
    node.prev = new_node
    return new_node

  while index - 1:
    node = node.next
    index -= 1

  next_node = node.next
  node.next = new_node
  new_node.next = next_node
  new_node.prev = node
  next_node.prev = new_node

  return head


head = Node(' '.join(array.pop(numberLines - 1)[1:]))
array.sort(key=lambda item: int(item[0]))

for node in array:
  head = insertNode(head, int(node[0]) - 1, ' '.join(node[1:]))

printList(head)

  
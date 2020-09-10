f = open('troughtful.txt', 'r')

numberLines = int(f.readline())
array = list(map(lambda item: item.rstrip().rsplit(), f.readlines()))
lastItem = array.pop()[0]
array = sorted(array)

class Node:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

  def __str__(self):
    return self.value

def printList(node):

  while node != None:
    print(node)
    node = node.next

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


head = Node(' '.join(array.pop(numberLines - 1)[1:]))
array.sort(key=lambda item: int(item[0]))

for node in array:
  head = insertNode(head, int(node[0]) - 1, ' '.join(node[1:]))

printList(head)
print(findNode(head, lastItem))

  
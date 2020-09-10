f = open('todolistdel.txt', 'r')

numberLines = int(f.readline())
array = list(map(lambda string: string.rstrip().rsplit(), f.readlines()))
deleteOrder = int(''.join(array.pop()))

class Node:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

  def __str__(self):
    return self.value

def printNode(node):

  if node == None:
    return

  while True:
    print(node)

    if node.next == None:
      break

    node = node.next

def insertNode(node, index, value):

  head = node
  new_node = Node(value)

  if index == 0:
    new_node.next = head
    return new_node

  while index - 1:
    node = node.next
    index -= 1

  next_node = node.next
  node.next = new_node
  new_node.next = next_node

  return head

def deleteNode(node, index):

  if index == 0:
    return node.next

  head = node

  while index:
    if index == 1:
      pre_node = node

    node = node.next
    index -= 1

  pre_node.next = node.next
  
  return head


# init head node
array = sorted(array)
last_elem = array.pop(numberLines - 1)
array.sort(key=lambda item: int(item[0]))
head = Node(' '.join(last_elem[1:]))


for node in array:
  head = insertNode(head, int(node[0]) - 1, ' '.join(node[1:]))

head = deleteNode(head, deleteOrder)
printNode(head)
  


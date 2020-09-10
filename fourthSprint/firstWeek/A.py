class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def solution(node, mX=-1000000):
  if node.left:
    mX = solution(node.left, mX)
  if node.right:
    mX = solution(node.right, mX)

  if mX < node.value:
    mX = node.value
  return mX

def fillTree(array):
  node = Node(array[0])
  head = node

  for item in array[1:]:
    while True:
      if item > node.value:
        if node.right is None:
          node.right = Node(item)
          break
        else:
          node = node.right

      elif item < node.value:
        if node.left is None:
          node.left = Node(item)
          break
        else:
          node = node.left
    
    node = head


  return node

# f = open('A.txt', 'r')
# array = list(map(int, f.readline().strip().split()))

# head = fillTree(array)

# print(solution(head, head.value))


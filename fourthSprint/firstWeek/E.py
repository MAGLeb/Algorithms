class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def solution(first, second, answer=True):
  if not answer:
    return False

  if first.left and second.left:
    answer = solution(first.left, second.left, answer)
  elif (first.left and not second.left) or (not first.left and second.left):
    return False

  if first.right and second.right:
    answer = solution(first.right, second.right, answer)
  elif (first.right and not second.right) or (not first.right and second.right):
    return False

  if first.value != second.value:
    return False

  return answer
 
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

f = open('E.txt', 'r')
array_first = list(map(int, f.readline().strip().split()))
array_second = list(map(int, f.readline().strip().split()))

first = fillTree(array_first)
second = fillTree(array_second)

print(solution(first, second))


from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def solution(node):
  result = []

  first_q = deque()
  second_q = deque()

  first_q.append(node)

  while True:
    intermediate = []

    while first_q:
      current = first_q.popleft()
      intermediate.append(current.value)

      if current.left:
        second_q.append(current.left)
      if current.right:
        second_q.append(current.right)

    result.append(intermediate)

    intermediate = []
    first_q.clear()

    while second_q:
      current = second_q.popleft()
      intermediate.append(current.value)

      if current.left:
        first_q.append(current.left)
      if current.right:
        first_q.append(current.right)

    result.append(intermediate)

    second_q.clear()

    if not first_q and not second_q:
      break

  return result


# def fillTree(array):
#   node = Node(array[0])
#   head = node

#   for item in array[1:]:
#     while True:
#       if item > node.value:
#         if node.right is None:
#           node.right = Node(item)
#           break
#         else:
#           node = node.right

#       elif item < node.value:
#         if node.left is None:
#           node.left = Node(item)
#           break
#         else:
#           node = node.left
    
#     node = head


#   return node

# f = open('A.txt', 'r')
# array = list(map(int, f.readline().strip().split()))

# print(solution(fillTree(array)))


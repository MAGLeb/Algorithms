from collections import deque
import random

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def solution(node):
  results = []

  first_deque = deque()
  second_deque = deque()

  first_deque.append(node)

  while True:

    if first_deque:
      results.append(first_deque[0].value)

    while first_deque:
      current = first_deque.popleft()

      if current.left:
        second_deque.append(current.left)
      if current.right:
        second_deque.append(current.right)

    if second_deque:
      results.append(second_deque[0].value)

    while second_deque:
      current = second_deque.popleft()

      if current.left:
        first_deque.append(current.left)
      if current.right:
        first_deque.append(current.right)

    if not first_deque and not second_deque:
      break

  return results

# def fillTree(array):
#   node = Node(array[0])
#   head = node

#   for item in array[1:]:
#     while True:
#       if random.randrange(2) == 0:
#         if node.right is None:
#           node.right = Node(item)
#           break
#         else:
#           node = node.right

#       else:
#         if node.left is None:
#           node.left = Node(item)
#           break
#         else:
#           node = node.left
    
#     node = head


#   return node


# f = open('A.txt', 'r')
# array = list(map(int, f.readline().strip().split()))

# head = fillTree(array)

# print(solution(head))
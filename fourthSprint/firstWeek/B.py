from collections import deque
import random

class Node:
  def __init__(self, value, right=None, left=None):
    self.value = value
    self.left = left
    self.right = right


def solution(node, answer=True):
  if not answer:
    return answer

  mLright = 0
  mLleft = 0

  if node.right:
    mLright = newFindDepth(node.right) + 1
  if node.left:
    mLleft = newFindDepth(node.left) + 1

  if abs(mLright - mLleft) > 1:
    answer = False
  if node.left:
    answer = solution(node.left, answer)
  if node.right:
    answer = solution(node.right, answer)

  return answer

def newFindDepth(node, mLleft=0, mLright=0):
  if node.left and node.right:
    left = newFindDepth(node.left, mLleft + 1, mLright)
    right = newFindDepth(node.right, mLleft, mLright + 1)
    return left if left > right else right

  else:
    if node.left:
      return newFindDepth(node.left, mLleft + 1, mLright)
    
    if node.right:
      return newFindDepth(node.right, mLleft, mLright + 1)

  return mLleft + mLright


def findDepth(node):
  result = 0

  first_q = deque()
  second_q = deque()

  first_q.append(node)

  while True:

    if first_q:
      result += 1

    while first_q:
      current = first_q.popleft()

      if current.left:
        second_q.append(current.left)
      if current.right:
        second_q.append(current.right)

    if second_q:
      result += 1

    while second_q:
      current = second_q.popleft()

      if current.left:
        first_q.append(current.left)
      if current.right:
        first_q.append(current.right)

    if not first_q and not second_q:
      break
    
  return result

  
def fillTree(array):
  node = Node(array[0])
  head = node

  for item in array[1:]:
    while True:
      if random.randrange(2) == 0:
        if node.right is None:
          node.right = Node(item)
          break
        else:
          node = node.right

      else:
        if node.left is None:
          node.left = Node(item)
          break
        else:
          node = node.left
    
    node = head


  return node


f = open('A.txt', 'r')
array = list(map(int, f.readline().strip().split()))

head = fillTree(array)

print(solution(head))
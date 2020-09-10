class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    results = []

    node = self

    while node:
      results.append(node.value)
      node = node.right

    return ' '.join(map(str, results))


def solution(node, answer=True):

  if node.left:
    if node.value <= node.left.value:
      return False
    answer = solution(node.left, answer)
  
  if node.right:
    if node.value >= node.right.value:
      return False
    answer = solution(node.right, answer)

  return answer


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


#   return head


# f = open('A.txt', 'r')
# array = list(map(int, f.readline().strip().split()))

# head = fillTree(array)

# print(solution(head))
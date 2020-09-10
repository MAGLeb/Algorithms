class Node:
  def __init__(self, value, right=None, left=None):
    self.value = value
    self.left = left
    self.right = right


def solution(node, mLleft=0, mLright=0):

  if node.left and node.right:
    left = solution(node.left, mLleft + 1, mLright)
    right = solution(node.right, mLleft, mLright + 1)
    return left if left > right else right

  if node.left:
    return solution(node.left, mLleft + 1, mLright)

  if node.right:
    return solution(node.right, mLleft, mLright + 1)

  return mLleft + mLright + 1

  


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
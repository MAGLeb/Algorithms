class Node:
  def __init__(self, value, right=None, left=None):
    self.value = value
    self.left = left
    self.right = right


def solution(node, value='', result=0):
  if not node.left and not node.right:
    result += int(value + str(node.value))
    return result
  
  if node.left:
    result = solution(node.left, value + str(node.value), result)

  if node.right:
    result = solution(node.right, value + str(node.value), result)

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


#   return head


# f = open('A.txt', 'r')
# array = list(map(int, f.readline().strip().split()))

# head = fillTree(array)

# print(solution(head))
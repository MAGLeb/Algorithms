# 15 авг 2020, 19:57:33 33776728 A Python 3.7.3

import math

f = open('input.txt', 'r')
n = int(f.readline())


def solution(number):
    return int((math.factorial(2 * number)) / ((math.factorial(number + 1)) * (math.factorial(number))))


print(solution(n))

# def solution_recursion(n):
#   if n == 0 or n == 1:
#     return 1

#   result = 0
#   for i in range(1, n+1):
#     result += solution_recursion(i-1) * solution_recursion(n-i)

#   return result

# print(solution_recursion(n))


# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right

# class Forest:
#   def __init__(self):
#     self.trees = []

#   def addTree(self, array):
#     node = Node(array[0])
#     head = node

#     for item in array[1:]:
#       while True:
#         if item > node.value:
#           if node.right is None:
#             node.right = Node(item)
#             break
#           else:
#             node = node.right

#         elif item < node.value:
#           if node.left is None:
#             node.left = Node(item)
#             break
#           else:
#             node = node.left

#       node = head

#     counter = 0

#     for tree in self.trees:
#       if counter > 0:
#         break

#       if self.checkForTwins(tree, head):
#         counter += 1

#     if counter == 0:
#       self.trees.append(node)

#   def checkForTwins(self, first, second, answer=True):
#     if not answer:
#       return False

#     if first.left and second.left:
#       answer = self.checkForTwins(first.left, second.left, answer)
#     elif (first.left and not second.left) or (not first.left and second.left):
#       return False

#     if first.right and second.right:
#       answer = self.checkForTwins(first.right, second.right, answer)
#     elif (first.right and not second.right) or (not first.right and second.right):
#       return False

#     if first.value != second.value:
#       return False

#     return answer

#   def countOfForest(self):
#     return len(self.trees)

# results = []
# residuals = []

# for i in range(2, 8):
#   forest = Forest()

#   for tree in list(itertools.permutations(range(1, i + 1), i)):
#     forest.addTree(tree)

#   answer = forest.countOfForest()

#   results.append(answer)
#   residuals.append(answer - 2*(math.factorial(i-1)))

# print(results, residuals)

### 17 авг 2020, 16:59:34 33786474	B

# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# head = Node(-1)
# head.left = Node(2)
# head.right = Node(3)
# head.right.right = Node(0)
# head.right.left = Node(4)
# head.left.right = Node(3)
# head.left.left = Node(7)
# head.left.right.right = Node(-6)
# head.left.right.left = Node(9)
# head.left.left.left = Node(-1)
#
# head = Node(2)
# head.left = Node(2)
# head.right = Node(-3)
# head.right.right = Node(1)
# head.right.left = Node(5)


def solution(node):
    max_result = float('-inf')

    def find_branch_max(current):
        nonlocal max_result
        results = [current.value]
        left_max = 0
        right_max = 0

        if current.left is not None:
            left_max = find_branch_max(current.left)
            results.append(left_max + current.value)

        if current.right is not None:
            right_max = find_branch_max(current.right)
            results.append(right_max + current.value)

        branch_max = max(results)
        node_max = max(left_max + current.value + right_max, branch_max)

        if node_max > max_result:
            max_result = node_max

        return branch_max

    find_branch_max(node)

    return max_result


# print(solution(head))

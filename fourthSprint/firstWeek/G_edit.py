f = open('G.txt', 'r')

n = int(f.readline())
array_first = list(map(int, f.readline().strip().split()))

m = int(f.readline())
array_second = list(map(int, f.readline().strip().split()))

k = int(f.readline())

# class Heap:
#   def __init__(self, array=[]):
#     self.items = []

#     for item in array:
#       self.add(item)

#   def add(self, item):
#     index = len(self.items)
#     self.items.append(item)
#     if self.items[index] 

#   def heapify(self):




def solution(first, second, k):
  index_array = [[0,0]]
  result_array = []

  while len(result_array) != k:

    min_sum = first[index_array[0][0]] + second[index_array[0][1]]
    index_first = index_array[0][0]
    index_second = index_array[0][1]
    index_to_del = 0

    for i, index in enumerate(index_array):
      inter_sum = first[index[0]] + second[index[1]]

      if inter_sum < min_sum:
        min_sum = inter_sum
        index_first = index[0]
        index_second = index[1]
        index_to_del = i
      elif inter_sum == min_sum:
        if index_first > index[0]:
          min_sum = inter_sum
          index_first = index[0]
          index_second = index[1]
          index_to_del = i

    result_array.append(sorted([first[index_first], second[index_second]]))


    index = index_array[index_to_del]
    counter = 0

    if index[0] + 1 < len(first):
      inter = [index[0] + 1, index[1]]
      if inter not in index_array:
        for ind in index_array:
          if inter[0] == ind[0]:
            if inter[1] >= ind[1]:
              counter = 1
              break
        if counter != 1:
          index_array.append(inter)

    counter = 0
              
    if index[1] + 1 < len(second):
      inter = [index[0], index[1] + 1]
      if inter not in index_array:
        for ind in index_array:
          if inter[1] == ind[1]:
            if inter[0] >= ind[0]:
              counter = 1
              break
        if counter != 1:
          index_array.append(inter)

    del index_array[index_to_del]

  return result_array


def print_solution(solution):
  for item in sorted(solution, key=lambda x: x[0]):
    print(' '.join(list(map(str, item))))


print_solution(solution(array_first, array_second, k))
        



# def solution_n_2(first, second, k):
#   intermediate = []
#   results= []

#   for index, item_i in enumerate(first):
#     for item_j in second:
#       intermediate.append([item_i, item_j, index])

#   intermediate.sort(key=lambda x: x[0] + x[1])
#   i = 0

#   while i < len(intermediate) - 1:
#     if sum(intermediate[i][:2]) == sum(intermediate[i+1][:2]):
#       if intermediate[i][2] < intermediate[i+1][2]:
#         inter = intermediate[i]
#         intermediate[i] = intermediate[i+1]
#         intermediate[i+1] = inter
#         j = i + 1
#         if j + 1 == len(intermediate):
#           break

#         while sum(intermediate[j][:2]) == sum(intermediate[j+1][:2]):
#           inter = intermediate[j]
#           intermediate[j] = intermediate[j+1]
#           intermediate[j+1] = inter
#           j += 1
#           if j + 1 == len(intermediate):
#             break
#       else:
#         i += 1



#     else:
#       i += 1

#   for item in intermediate:
#     results.append(sorted(item[:2]))

#   return results[:k]


# def quiquSort(array):
#   if len(array) < 2:
#     return array

#   mid = array[0]

#   left = [item for item in array[1:] if item[0] <= mid[0]]
#   right = [item for item in array[1:] if item[0] > mid[0]]

#   return quiquSort(left) + [mid] + quiquSort(right)

# def mergedSort(array):

#   if len(array) == 1:
#     return array

#   left = mergedSort(array[int(len(array) / 2):])
#   right = mergedSort(array[:int(len(array) / 2)])
#   return compairArrays(right, left)


# def compairArrays(first, second):
#   result = []
#   i, j = 0, 0

#   while len(result) != len(first) + len(second):
#     if i == len(first):
#       result.append(second[j])
#       j += 1
#       continue

#     if j == len(second):
#       result.append(first[i])
#       i += 1
#       continue

#     if first[i] < second[j]:
#       result.append(first[i])
#       i += 1
#     else:
#       result.append(second[j])
#       j += 1

#   return result


        


# print_solution(solution_n_2(array_first, array_second, k))
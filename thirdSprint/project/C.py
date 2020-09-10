### 11 июл 2020, 23:26:40 33621114 C Python 3.7.3
### 18 июл 2020, 09:28:35 33651302 C Python 3.7.3

f = open('input.txt', 'r')

n = int(f.readline())
array = list(map(lambda x: list(x), f.readline().strip().split()))


def radixSort(array, k=6):

  for j in range(k-1, -1, -1):
    interm_array = [[] for i in range(10)]

    for item in array:
      if len(item) != k:
        index = j - k + len(item)
        if index >= 0 and index < len(item):
          interm_array[int(item[index])].append(item)
        else:
          interm_array[0].append(item)
      else:
        interm_array[int(item[j])].append(item)

    array = []

    for item in interm_array:
      array += item

  return array

print(' '.join(map(str, map(int, (map(lambda x: ''.join(x), radixSort(array)))))))




















# def checkAnswer(array):
#   for i in range(len(array) - 1):
#     first = int(''.join(array[i]))
#     second = int(''.join(array[i + 1]))
#     if int(''.join(array[i + 1])) - int(''.join(array[i])) < 0:
#       print(first, second)
#       return False
#   return True

# print(checkAnswer(answer))





# def radixSort(array):

#   for i in range(len(array)):
#     for j in range(len(array) - 1):
#       if len(array[j]) > len(array[j + 1]):
#         intermediate = array[j]
#         array[j] = array[j + 1]
#         array[j + 1] = intermediate
#       elif len(array[j]) == len(array[j + 1]):
#         if array[j][0] > array[j + 1][0]:
#           intermediate = array[j]
#           array[j] = array[j + 1]
#           array[j + 1] = intermediate
#         elif array[j][0] == array[j + 1][0]:
#           if len(array[j]) == 2:
#             if array[j][1] > array[j + 1][1]:
#               intermediate = array[j]
#               array[j] = array[j + 1]
#               array[j + 1] = intermediate
#           elif len(array[j]) == 3:
#             if array[j][1] > array[j + 1][1]:
#               intermediate = array[j]
#               array[j] = array[j + 1]
#               array[j + 1] = intermediate
#             elif array[j][1] == array[j + 1][1]:
#               if array[j][2] > array[j + 1][2]:
#                 intermediate = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = intermediate

#   return array



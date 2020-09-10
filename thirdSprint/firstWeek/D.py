f = open('D.txt', 'r')
n = int(f.readline())
m = int(f.readline())

arrayFirst = list(map(int, f.readline().strip().split()))
arraySecond = list(map(int, f.readline().strip().split()))


def quickSort(array):

  if len(array) < 2:
    return array

  pivot = array[0]
  less = [item for item in array[1:] if item <= pivot]
  more = [item for item in array[1:] if item > pivot]

  return quickSort(less) + [pivot] + quickSort(more)

def findNumberInArray(array, n):

  if len(array) == 0:
    return False

  if len(array) == 1:
    if array[0] == n:
      return True
    else:
      return False

  if array[int(len(array) / 2)] == n:
    return True
  elif array[int(len(array) / 2)] > n:
    return findNumberInArray(array[:int(len(array) / 2)], n)
  else:
    return findNumberInArray(array[int(len(array) / 2):], n)

def findNumberInArrayN(array, n):

  for item in array:
    if item == n:
      return True
  
  return False

def findSimilarity(first, second):

  result = []

  if len(first) == 0 or len(second) == 0:
    return result

  sortedSecond = quickSort(second)

  for number in first:
    if findNumberInArray(sortedSecond, number):
      if findNumberInArrayN(result, number):
        continue
      sortedSecond.remove(number)
      result.append(number)

  return result

print(' '.join(map(str, findSimilarity(arrayFirst, arraySecond))))

















# def findSimilarity(arrayFirst, arraySecond):
#   result = []
#   j = 0

#   if len(arrayFirst) > len(arraySecond):
#     first = arrayFirst
#     second = arraySecond
#   else:
#     first = arraySecond
#     second = arrayFirst

#   for i in range(len(first)):

#     if j >= len(second):
#       break

#     while first[i] > second[j]:
#       j += 1
#       if j >= len(second):
#         break

#     if j >= len(second):
#       break
    
#     if first[i] == second[j]:
#       result.append(first[i])
#       j += 1

  
#   return ' '.join(map(str, result))


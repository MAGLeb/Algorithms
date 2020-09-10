f = open('G.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().strip().split()))

def mergedSort(array):

  if len(array) == 1:
    return array

  left = mergedSort(array[int(len(array) / 2):])
  right = mergedSort(array[:int(len(array) / 2)])
  return compairArrays(right, left)


def compairArrays(first, second):
  result = []
  i, j = 0, 0

  while len(result) != len(first) + len(second):
    if i == len(first):
      result.append(second[j])
      j += 1
      continue

    if j == len(second):
      result.append(first[i])
      i += 1
      continue

    if first[i] < second[j]:
      result.append(first[i])
      i += 1
    else:
      result.append(second[j])
      j += 1

  return result

def findMaxPer(sortedArray):

  for i in reversed(range(2, len(sortedArray))):
    twoSides = sortedArray[i - 2] + sortedArray[i - 1]
    if twoSides > sortedArray[i]:
      return twoSides + sortedArray[i]
      
  return -1



print(findMaxPer(mergedSort(array)))
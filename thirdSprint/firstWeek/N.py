f = open('N.txt', 'r')

m = int(f.readline())
n = int(f.readline())
matrix = []

line = list(map(int, f.readline().strip().split()))

while line:
  matrix.append(line)
  line = list(map(int, f.readline().strip().split()))



def matrixToDiags(matrix, m, n):

  # under middle diag sorted diags
  array = []
  i = m - 1
  j = 0

  while i != 0:
    r = i
    l = j
    while True:
      array.append(matrix[r][l])
      if r == m - 1 or l == n - 1:
        r = i
        l = j
        i -= 1
        break

      r += 1
      l += 1
    
    array = merge(array)
    for item in array:
      matrix[r][l] = item
      r += 1
      l += 1
    
    array = []

  # middle diag sorted
  r = i
  l = j

  while True:
    if r == m or l == n:
      break

    array.append(matrix[r][l])
    r += 1
    l += 1

  array = merge(array)

  r = i
  l = j
  for item in array:
    matrix[r][l] = item
    r += 1
    l += 1

  # above middle diag sorted diags

  array = []

  while j != n:
    r = i
    l = j
    while True:
      array.append(matrix[r][l])
      if r == m - 1 or l == n - 1:
        r = i
        l = j
        j += 1
        break

      r += 1
      l += 1
    
    array = merge(array)
    for item in array:
      matrix[r][l] = item
      r += 1
      l += 1
    
    array = []

    
  
  return matrix


def quiqeSort(array):

  if len(array) < 2:
    return array

  pivot = array[0]
  left = [item for item in array[1:] if item <= pivot]
  right = [item for item in array[1:] if item > pivot]

  return quiqeSort(left) + [pivot] + quiqeSort(right)

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

def merge(array):

  if len(array) < 2:
    return array

  p = int(len(array) / 2)
  right = merge(array[p:])
  left = merge(array[:p])

  return compairArrays(left, right)


for array in matrixToDiags(matrix, m, n):
  print(' '.join(map(str, array)))



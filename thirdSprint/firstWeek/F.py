f = open('F.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().strip().split()))

def devideForTwoArrays(array):
  first, second = [], []

  for item in array:
    if item % 2 == 0:
      first.append(item)
    else:
      second.append(item)

  return first, second

def compairArrays(first, second):
  result = []

  for i in range(len(first)):
    result.append(first[i])
    result.append(second[i])

  return result

first, second = devideForTwoArrays(array)

print(' '.join(map(str, compairArrays(first, second))))
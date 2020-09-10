f = open('K.txt', 'r')

n = int(f.readline())
array = list(map(int, f.readline().strip().split()))


def findMax(array):
  mx = array[0]

  for i in range(1, len(array)):
    if mx < array[i]:
      mx = array[i]
  
  return mx

def findMin(array):
  mn = array[0]

  for i in range(1, len(array)):
    if mn > array[i]:
      mn = array[i]

  return mn


def findNumberOfSlices(array):
  result = 0
  start = 0
  end = 1

  while end < len(array):
    
    if findMax(array[start:end]) <= findMin(array[end:]):
      start = end
      end += 1
      result += 1
    else:
      end += 1

  result += 1

  return result

print(findNumberOfSlices(array))
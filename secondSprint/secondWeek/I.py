f = open('I.txt', 'r')
n = int(f.readline())
m = int(f.readline())
array = list(map(int, f.readline().split()))
total = sum(array) / n

def findSum(array):

  if len(array) == 0:
    return True

  sum = 0
  index = []

  for i in range(len(array)):
    if array[i] + sum <= total:
      sum += array[i]
      index.append(i)
    
    if sum == total:
      break

  if sum != total:
    return False
  else:
    return findSum(list(map(lambda x: x[1], list(filter(lambda x: x[0] not in index, enumerate(array))))))

print(findSum(array))
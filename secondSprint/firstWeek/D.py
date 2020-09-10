f = open('D.txt', 'r')
weightOfBag = int(f.readline())
numberItems = int(f.readline())
array = list(map(lambda line: list(map(int, line.strip().split())), f.readlines()))
indexes = []

def findItem(array, indexes, weightOfBag):
  result = [-1, -1]
  index = -1

  for i in range(len(array)):
    if i not in indexes:
      if array[i][1] <= weightOfBag:
        if array[i][0] > result[0]:
          result = array[i]
          index = i
        elif array[i][0] == result[0]:
          if array[i][1] < result[1]:
            result = array[i]
            index = i

  if index != -1:
    indexes.append(index)
  return result

def findIndexItems(array, weightOfBag):

  while True:
    item = findItem(array, indexes, weightOfBag)

    if item == [-1, -1]:
      break

    weightOfBag -= item[1]

  return ' '.join(map(str, sorted(indexes)))
    

print(findIndexItems(array, weightOfBag))











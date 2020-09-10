f = open('H.txt', 'r')

m = int(f.readline())
array = []

line = f.readline()
while line:
  array.append(list(map(int, line.strip().split())))
  line = f.readline()


def quiqeSortDoubleArray(array):

  if len(array) < 2:
    return array

  pivot = array[0]

  left = [item for item in array[1:] if item[0] <= pivot[0]]
  right = [item for item in array[1:] if item[0] > pivot[0]]

  return quiqeSortDoubleArray(left) + [pivot] + quiqeSortDoubleArray(right)

def findFlowerbed(array):
  results = []
  intermediate = array[0]

  for i in range(1, len(array)):

    if intermediate[1] >= array[i][0]:
      if intermediate[1] < array[i][1]:
        intermediate[1] = array[i][1]

    else:
      results.append(intermediate)
      intermediate = array[i]

    if i + 1 == len(array):
      results.append(intermediate)

  return results



result = list(map(lambda x: list(map(str, x)), findFlowerbed(quiqeSortDoubleArray(array))))

for item in result:
  print(' '.join(item))






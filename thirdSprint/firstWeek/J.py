f = open('J.txt', 'r')

n = int(f.readline())
array = list(map(int, f.readline().strip().split()))
m = int(f.readline())
sample = list(map(int, f.readline().strip().split()))

def quiqeSort(array):
  if len(array) < 2:
    return array

  pivot = array[0]
  left = [item for item in array[1:] if item <= pivot]
  right = [item for item in array[1:] if item > pivot]

  return quiqeSort(left) + [pivot] + quiqeSort(right)

resultOther = []
resultSample = []
result = []
objectSample = dict()


for item in sample:
  objectSample[item] = 0

for number in array:
  if number in objectSample:
    objectSample[number] += 1
  else:
    resultOther.append(number)

for key, value in objectSample.items():
  for i in range(value):
    result.append(int(key))

resultOther = quiqeSort(resultOther)

for number in resultOther:
  result.append(number)

print(' '.join(map(str, result)))





f = open('A.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().rstrip().rsplit()))

def quickSort(array):

  if len(array) < 2:
    return array

  pivot = array[0]
  less = [item for item in array[1:] if item <= pivot]
  more = [item for item in array[1:] if item > pivot]

  return quickSort(less) + [pivot] + quickSort(more)


print(' '.join(map(str, quickSort(array))))

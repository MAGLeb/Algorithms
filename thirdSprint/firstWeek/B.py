f = open('A.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().rstrip().rsplit()))



def insertSort(array):

  for j in range(1, len(array)):
    for i in range(j):
      if array[j] < array[i]:
        intermediate = array[i]
        array[i] = array[j]
        array[j] = intermediate

  return ' '.join(map(str, array))

print(insertSort(array))

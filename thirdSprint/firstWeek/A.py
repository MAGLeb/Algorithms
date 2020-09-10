f = open('A.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().rstrip().rsplit()))

def bubbleSort(array):

  counter = 0

  while True:
    counter = 0  
    for i in range(1, len(array)):
      if array[i - 1] > array[i]:
        intermediate = array[i - 1]
        array[i - 1] = array[i]
        array[i] = intermediate
        counter += 1

    if counter == 0:
      break
  
  return ' '.join(map(str, array))

print(bubbleSort(array))


f = open('muchcode.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().split()))


def maxArraySum(array):
  new_array = []
  i = 0

  while i != len(array):
    sum = 0

    while array[i] >= 0:
      sum += array[i]
      i += 1
      if i == len(array):
        break
    
    if sum != 0:
      new_array.append(sum)
      sum = 0
      if i == len(array):
        break

    while array[i] <= 0:
      sum += array[i]
      i += 1
      if i == len(array):
        break

    if sum != 0:
      new_array.append(sum)
  print(new_array)
  return new_array

def localMin():
  result = array[0]

  for i in range(1, len(array)):
    if array[i] > result:
      result = array[i]

  return result


def maxSum(array):

  if len(array) == 1:
    if array[0] < 0:
      return localMin()
    else:
      return array[0]
    
  if array[0] > 0:
    max_result = array[0]
    j = 1
  else:
    max_result = array[1]
    j = 2

  inter_sum = 0

  while j < len(array) - 1:
    if max_result + array[j] < 0:
      max_result = array[j+1]
      j += 2
    else:
      inter_sum += array[j] + array[j+1]

      if max_result + inter_sum > max_result:
        max_result = max_result + inter_sum
        inter_sum = 0


      if array[j+1] > max_result:
        max_result = array[j+1]
        inter_sum = 0

      j += 2

  return max_result

print(maxSum(maxArraySum(array)))

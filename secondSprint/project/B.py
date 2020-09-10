# 17 июн 2020, 20:08:23 33504797
# I don't know how creating function will help to make easy this code. If you have some ideas how to do it, tell me in next review with more details. And if you want to help me, give me idea about new algorithm, if it is not correct, but it work.

f = open('input.txt', 'r')
n = int(f.readline())
k = int(f.readline())
array = list(map(int, f.readline().rstrip().rsplit()))

def recursive(start, end):

  # when len(array) <= 1, check for finding number 'k'
  if start >= end:
    if k == array[start]:
      return start
    else:
      return -1

  # if number of items in array even, then mid = len(array) / 2 + 1 else middle elemnt
  if (start + end) % 2 == 0:
    mid = int((start + end) / 2)
  else:
    mid = int((start + end) / 2) + 1

  # check for finding number (start, end and middle of given array)
  if array[mid] == k:
    return mid
  elif array[start] == k:
    return start
  elif array[end] == k:
    return end
  
  # after just look at the algorithm. I check for less or more start, end and mid.
  if array[mid] > k:
    if array[start] < k:
      return recursive(start + 1, mid - 1)
    elif array[start] > array[end]:
      if array[start] < array[mid] and array[end] < array[mid]:
        return recursive(mid + 1, end - 1)
      return recursive(start + 1, mid - 1)
    else:
      return recursive(mid + 1, end - 1)
      
  else:
    if array[mid] > array[start] and array[mid] > array[end]:
      if array[start] < array[end]:
        return recursive(start + 1, mid - 1)
      else:
        return recursive(mid + 1, end - 1)
    elif array[mid] < array[start] and array[mid] < array[end]:
      if array[start] > array[end]:
        if array[start] > k and array[end] > k:
          return recursive(mid + 1, end - 1)
        return recursive(start + 1, mid - 1)
      else:
        return recursive(mid + 1, end - 1)
    else:
      return recursive(mid + 1, end - 1)


print(recursive(0, len(array) - 1))
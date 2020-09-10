### 3 июл 2020, 10:01:41 33579532	B Python 3.7.3
### 18 июл 2020, 09:29:47 33651303 B Python 3.7.3

f = open('input.txt', 'r')
n = int(f.readline())
m = int(f.readline())

array_1 = list(map(int, f.readline().strip().split()))
array_2 = list(map(int, f.readline().strip().split()))


def findMedian(first, second, n, m):
  i, j = 0, 0
  result = 0
  prev_result = 0
  mid = (n + m) // 2 + ((n + m) % 2)
  
  while True:
    if i + j - 1 == mid:
      break

    if i == n:
      prev_result = result
      result = second[j]
      j += 1
    elif j == m:
      prev_result = result
      result = first[i]
      i += 1

    elif first[i] <= second[j]:
      prev_result = result
      result = first[i]
      i += 1
    else:
      prev_result = result
      result = second[j]
      j += 1

  if (n + m) % 2 != 0:
    result = prev_result
  else:
    result = (result + prev_result) / 2

  if not result % 1:
    result = int(result)
  
  return result


print(findMedian(array_1, array_2, n, m))


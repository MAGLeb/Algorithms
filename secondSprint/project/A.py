# 17 июн 2020, 11:11:12 33500641

f = open('input.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().rstrip().split()))

def solution(array):
  result = 0
  array = sorted(array, reverse=True)
  
  if len(array) < 2:
    return 0

  while True:
    array[0] -= 1
    array[1] -= 1
    result += 1
    array = sorted(array, reverse=True)

    if array[0] == 0 or array[1] == 0:
      break
    
  return result

print(solution(array))

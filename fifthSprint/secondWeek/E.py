f = open('E.txt', 'r')

n = int(f.readline())
array = list(f.readline().strip().split())

# array = '1 0'.split()

def solution(array):
  minIndexArray = {}
  maxIndexArray = {}
  currentSum = 0

  minIndexArray[0] = currentSum

  for index, number in enumerate(array):
    if number == '0':
      currentSum += 1
    else:
      currentSum -= 1

    if currentSum not in minIndexArray:
      minIndexArray[currentSum] = index
    else:
      maxIndexArray[currentSum] = index

  maxResult = 0
  for key in minIndexArray.keys():
    if key in maxIndexArray:
      if maxIndexArray[key] - minIndexArray[key] > maxResult:
        maxResult = maxIndexArray[key] - minIndexArray[key]

  return maxResult + 1 if maxResult % 2 else maxResult



def solution_old(array):
  max_result = 0

  for i in range(len(array)):
    inter_result = 0
    counter = 0
    if max_result > len(array) - i:
      break
    for item in array[i:]:
      if item == '1':
        inter_result += 1
      else:
        inter_result -= 1
      counter += 1
      
      if inter_result == 0:
        if counter > max_result:
          max_result = counter
  
  return max_result


print(solution(array))
with open('H.txt', 'r') as f:
  n = int(f.readline().strip())
  firstArray = f.readline().strip().split()
  m = int(f.readline().strip())
  secondArray = f.readline().strip().split()

def solution_old(first, second, n, m):
  result = 0
  array = [[0 for i in range(m + 1)] for j in range(n + 1)]

  for i in range(n + 1):
    for j in range(m + 1):
      if (i == 0) or (j == 0):
        array[i][j] = 0
      elif first[i - 1] == second[j - 1]:
        array[i][j] = array[i - 1][j - 1] + 1
        result = max(result, array[i][j])
      else:
        array[i][j] = 0
  
  return result



def solution(first, second, n, m):

  for l in range(min(n, m), 0, -1):
    for i in range(n - l + 1):
      for j in range(m - l + 1):
        print(first[i:i+l], second[j:j+l])
        if first[i:i+l] == second[j:j+l]:
          return len(first[i:i+l]) 


print(solution(firstArray, secondArray, n, m))
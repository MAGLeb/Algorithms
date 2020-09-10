with open('O.txt', 'r') as f:
  n, m = list(map(int, f.readline().strip().split()))
  matrix = [[0] * (m + 2)]
  line = list(map(int, f.readline().strip().split()))
  while line:
    matrix.append([0] + line + [0])
    line = list(map(int, f.readline().strip().split()))
  matrix.append([0] * (m + 2))

def solution(matrix, n, m):
  totalResult = 0

  for i in range(1, n+1):
    for j in range(1, m+1):
      if matrix[i][j] == 1:
        if matrix[i-1][j] == 0:
          totalResult += 1
        if matrix[i][j-1] == 0:
          totalResult += 1
        if matrix[i+1][j] == 0:
          totalResult += 1
        if matrix[i][j+1] == 0:
          totalResult += 1

  return totalResult

print(solution(matrix, n, m))
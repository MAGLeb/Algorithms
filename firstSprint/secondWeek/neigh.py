f = open('neigh.txt', 'r')

n = int(f.readline())
m = int(f.readline())

matrix = []

for i in range(n):
  matrix.append(list(map(int, f.readline().split())))

a = int(f.readline())
b = int(f.readline())

result = []

if b + 1 < m:
  result.append(matrix[a][b + 1])

if b - 1 >= 0:
  result.append(matrix[a][b - 1])

if a - 1 >= 0:
  result.append(matrix[a - 1][b])

if a + 1 < n:
  result.append(matrix[a + 1][b])

print(' '.join(map(str, sorted(result))))

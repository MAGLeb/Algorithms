filename = 'matrix.txt'

f = open(filename, 'r')

n = int(f.readline())
m = int(f.readline())

matrix = []

for i in range(n):
  matrix.append(list(map(int, f.readline().split())))

f.close()

result = []

for i in range(m):
  line = []
  for j in range(n):
    line.append(matrix[j][i])
  
  result.append(line)

with open('output.txt', 'w') as f:
  for line in result:
    f.write(' '.join(map(str, line)) + '\n')
    
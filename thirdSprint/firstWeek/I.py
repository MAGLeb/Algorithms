f = open('I.txt', 'r')

n = int(f.readline())
array = list(map(int, f.readline().strip().split()))

result = []
counter = [0, 0, 0]

for item in array:
  counter[item] += 1

for i in range(len(counter)):
  c = counter[i]
  while c != 0:
    result.append(i)
    c -= 1


print(' '.join(map(str, result)))
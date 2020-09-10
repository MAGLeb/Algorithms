f = open('K.txt', 'r')

number = int(f.readline())
sizeOfMatissa = int(f.readline())
n = 0
r = 0

for i in range(number + 1):
  if i * i > number:
    n = i - 1
    r = n * n - number
    break

divisible = 2 * n * n + r
divider = 2 * n

x = divisible / divider

for i in range(sizeOfMatissa):
  x = 0.5 * (x + number / x)

print(format(x, '.5f'))
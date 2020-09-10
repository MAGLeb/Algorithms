# f = open('M.txt', 'r')
# a = int(f.readline())
# b = int(f.readline())
# f.close()

a = 12
b = 8

def findMGD(a, b):
  if a < b:
    if b % a == 0:
      return a
    else:
      return findMGD(a, b % a)
  else:
    if a % b == 0:
      return b
    else:
      return findMGD(b, a % b)

def coeficentes(a, b, c):
  x = 0
  y = 0

  while abs(x * a - y * b) != c:
    if a < b:
      if x * a > y * b:
        y += 1
      else:
        x += 1
    else:
      if x * a < y * b:
        x += 1
      else:
        y += 1

  if x * a > y * b:
    return x, -y, c
  else:
    return -x, y, c

print(' '.join(map(str, coeficentes(a, b, findMGD(a, b)))))

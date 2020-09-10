f = open('M.txt', 'r')
a = int(f.readline())
b = int(f.readline())
f.close()

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

print(findMGD(a, b))



f = open('O.txt', 'r')
a = int(f.readline())
b = int(f.readline())

sign = (a > 0 and b > 0) or (a < 0 and b < 0)

a = abs(a)
b = abs(b)


def divide(intermediate, counter = 1):

  if a < intermediate:
    return 0

  if intermediate + b >= a:
    return counter + 1 if intermediate + b == a else counter

  counter += 1
  intermediate += b
  return divide(intermediate, counter)


result = divide(b)

if sign:
  print(result)
else:
  print(-result)
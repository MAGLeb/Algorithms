f = open('ones.txt', 'r')
number = int(f.readline())


def findCountOnes(number):
  numberTenBase = bin(number)[2:]
  result = 0

  for item in numberTenBase:
    if item == '1':
      result += 1

  return result


print(findCountOnes(number))
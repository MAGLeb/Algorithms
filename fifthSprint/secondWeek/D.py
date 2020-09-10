# with open('D.txt', 'r') as f:
#   n = int(f.readline())
#   m = int(f.readline())

n = 1
m = 1


def solution(n, m):
    integerPart = str(n // m)
    fractionalPart = ''
    numerator = []

    n = (n % m) * 10

    while True:
        if n == 0:
          startOfPeriod = len(fractionalPart)
          break
        
        if n in numerator:
            startOfPeriod = numerator.index(n)
            break

        while n // m == 0:
            numerator.append(n)
            n *= 10
            fractionalPart += '0'
            

        numerator.append(n)
        fractionalPart += str(n // m)
        n = (n - n // m * m) * 10

    if fractionalPart:
      if startOfPeriod == len(fractionalPart):
        return integerPart + '.' + fractionalPart
      else:
        return integerPart + '.' + fractionalPart[:startOfPeriod] + '(' + fractionalPart[startOfPeriod:] + ')'
    else:
      return integerPart


print(solution(n, m))

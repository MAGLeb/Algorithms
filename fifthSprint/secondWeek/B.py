f = open('A.txt', 'r')
n = int(f.readline())

def solution_era_old(number):
  # решето Эратосфена
  results = []

  array = [item for item in range(number)]
  array[1] = 0

  i = 2

  while i < number:
    if array[i] != 0:
      results.append(array[i])
      for j in range(i, number, i):
        array[j] = 0
    i += 1

  return len(results)

def solution_era(number):
  # решето Эратосфена
  results = []

  array = [item for item in range(number)]
  array[1] = 0

  i = 2

  while i < number:
    if array[i] != 0:
      results.append(array[i])
      for j in range(i * i, number, i):
        array[j] = 0
    i += 1

  return len(results)


def solution(number):
  # решето Эратосфена LINEAR
  primes = []
  array = [0] * (n + 1)

  for i in range(2, n):
    if array[i] == 0:
      array[i] = i
      primes.append(i)
    for p in primes:
      if p * i > n:
        break
      array[p * i] = p

  return len(primes)




def isPrime(number):
  if number < 2:
    return False
  if number < 4:
    return True

  i = 2
  # while i < number:
  while i * i < number:
    if number % i == 0:
      return False
    i += 1

  return True

def solution_second(number):
  results = []
  i = 2

  while i < number:
    if isPrime(i):
      results.append(i)
    i += 1
    
  return len(results)



print(solution(n))


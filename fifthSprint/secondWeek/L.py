from itertools import combinations

f = open('L.txt', 'r')

n = int(f.readline())
mX = int(f.readline())
array = list(f.readline().strip().split())

def hashFunction(string):
  total = 0
  a = 5
  m = 113

  for letters in string:
    if int(letters) < 0:
      total = ord(letters[0]) 
      for letter in letters[1:]:
        total = ord(letter) + a * total
        total %= m
    else:
      for letter in letters:
        total = ord(letter) + a * total
        total %= m

    total %= m
  
  return total



def solution(mX, array):
  hashArray = []
  results = []

  for comb in combinations(array, 4):
    currentSum = sum(map(int, comb))
    if currentSum == mX:
      hashedSum = hashFunction(sorted(comb))
      if hashedSum not in hashArray:
        hashArray.append(hashedSum)
        results.append(sorted(list(map(int, comb))))

  return sorted(results)

results = solution(mX, array)

print(len(results))
for res in results:
  print(' '.join(list(map(str, res))))
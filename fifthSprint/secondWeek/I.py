f = open('I.txt', 'r')

a = int(f.readline())
m = int(f.readline())
string = list(f.readline().strip())

def solution_old(a, m, string):
  total = 0

  for index, letter in enumerate(string):
    total += ord(letter) * a ** (len(string) - index - 1)

  return total % m

def solution(a, m, string):
  beta = 0

  for letter in string:
    beta = ord(letter) + beta * a
    if beta > m:
      beta %= m

  return beta



print(solution(a, m, string))


with open('N.txt', 'r') as f:
  string = f.readline().strip()

def solution(string):
  dictionary = {}
  totalResult = 0

  for letter in string:
    if letter in dictionary:
      dictionary[letter] += 1
      if dictionary[letter] == 2:
        totalResult += 2
        del dictionary[letter]
    else:
      dictionary[letter] = 1

  if dictionary:
    return totalResult + 1
  else:
    return totalResult

print(solution(string))
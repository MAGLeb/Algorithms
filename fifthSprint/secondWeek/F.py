with open('F.txt', 'r') as f:
  firstString = f.readline().strip()
  secondString = f.readline().strip()

def solution(pattern, string):
  dictionary = {}
  uniq = []

  if len(pattern) != len(string):
    return 'NO'

  for index, letter in enumerate(pattern):
    if letter in dictionary:
      if dictionary[letter] != string[index]:
        return 'NO'
    else:
      if string[index] in uniq:
        return 'NO'
      else:
        uniq.append(string[index])
        dictionary[letter] = string[index]
  
  return 'YES'


print(solution(firstString, secondString))
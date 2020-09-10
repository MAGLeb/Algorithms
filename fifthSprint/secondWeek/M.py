with open('M.txt', 'r') as f:
  pattern = f.readline().strip()
  string = f.readline().strip().split()

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

print(solution(pattern, string))

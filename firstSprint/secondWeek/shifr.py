from collections import defaultdict

f = open('shifr.txt', 'r')
string = f.readline().rstrip()
shablon = f.readline().rstrip()  

def removeAddDict(rem, letter, dictionary):

  if dictionary[rem] == 1:
    dictionary.pop(rem)
  else:
    dictionary[rem] -= 1
  

  if letter in dictionary:
    dictionary[letter] += 1
  else:
    dictionary[letter] = 1


  return dictionary



size_shablon = len(shablon)
size_string = len(string)

anagram = defaultdict(int)
new_string = defaultdict(int)

for k in string[0:size_shablon]:
  new_string[k] += 1

for k in shablon:
  anagram[k] += 1

result = 0




if new_string == anagram:
  result += 1

for i in range(size_shablon - 1, size_string - 1):
 
  if removeAddDict(string[i - size_shablon + 1], string[i + 1], new_string) == anagram:
    result += 1

print(result)
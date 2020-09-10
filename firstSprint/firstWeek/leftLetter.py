f = open('leftLetter.txt', 'r')
first = sorted(f.readline().strip())
second = sorted(f.readline().strip())

def leftLetter(first, second):
  for i in range(len(first)):
    if first[i] != second[i]:
      return second[i]

  return second[len(second) - 1]      


print(leftLetter(first, second))

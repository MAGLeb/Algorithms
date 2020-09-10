filename = 'C.txt'

with open(filename, 'r') as f:
  s = f.readline().strip()
  t = f.readline().strip()


def func():
  i = 0
  j = 0

  if len(s) == 0:
    return True

  while j != len(t):

    if s[i] == t[j]:
      i += 1
    
    j += 1

    if i == len(s):
      return True
  
  return False

print(func())

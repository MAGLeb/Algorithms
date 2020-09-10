f = open('A.txt', 'r')
n = int(f.readline())

def recursive(result, opened, pair):

  if len(result) == n * 2:
    print(result)
    return

  if opened == 0:
    recursive(result + '(', opened + 1, pair + 1)
  elif pair == n:
    recursive(result + ')', opened - 1, pair)
  else:
    recursive(result + '(', opened + 1, pair + 1)
    recursive(result + ')', opened - 1, pair)

recursive('', 0, 0)
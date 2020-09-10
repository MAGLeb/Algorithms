f = open('G.txt', 'r')

letter = f.readline()

def recursive(let):
  if let == letter:
    print(let)
    return

  print(let, end=' ')
  recursive(chr(ord(let) + 1))

recursive('a')
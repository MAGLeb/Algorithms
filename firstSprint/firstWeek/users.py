f = open('users.txt', 'r')

firstIds = list(map(int, f.readline().split(' ')))
firstNumber = int(f.readline())
secondNumber = int(f.readline())
secondIds = list(map(int, f.readline().split(' ')))
firstNumber += secondNumber

# firstIds = list(map(int, '1 2 3 0 0 0'.split(' ')))
# firstNumber = int('6')
# secondNumber = int('3')
# secondIds = list(map(int, '2 5 6'.split(' ')))

j = 0

for i in range(firstNumber):

  if j == secondNumber:
    break

  buffer = 0

  if firstIds[i] == 0:
    firstIds[i] = secondIds[j]
    j += 1
    continue

  if secondIds[j] < firstIds[i]:
    buffer = firstIds[i]
    firstIds[i] = secondIds[j]


    for k in range(i + 1, firstNumber):
        secondBuffer = firstIds[k]
        firstIds[k] = buffer
        buffer = secondBuffer

    j += 1

print(' '.join(map(str, firstIds)))

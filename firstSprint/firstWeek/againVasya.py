f = open('vasya.txt', 'r')

firstIds = list(f.readline().split(' '))
firstNumber = int(f.readline())
secondNumber = int(f.readline())
secondIds = list(f.readline().split(' '))


for i in range(secondNumber):
	firstIds[i + firstNumber] = secondIds[i]

print(' '.join(map(str, sorted(map(int, firstIds)))))

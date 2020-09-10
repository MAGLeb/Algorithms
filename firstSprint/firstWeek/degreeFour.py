f = open('degreeFour.txt', 'r')
number = int(f.readline())
result = 4

while result < number:
	result = result * 4

if result == number or number == 1:
	print(True)
else:
	print(False)



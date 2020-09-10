lenght = input()
a = list(map(int, input().split(' ')))
i = 0

while i < len(a):
	if a[i] == 0:
		del a[i]
	else:
		i += 1



print(' '.join(map(str, a)))



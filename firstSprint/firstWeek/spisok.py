lenght = 5
array = '1 2 3 4 5'
k = 55

print(' '.join(list(str(int(''.join(map(str, array.split(' ')))) + k))))
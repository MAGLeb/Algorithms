with open('A.txt', 'r') as f:
    array = f.readline().strip().split()

print(' '.join(array[::-1]))
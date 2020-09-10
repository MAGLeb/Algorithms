number = input()
array = map(int, input().split(' ')[::-1])

# 10
# 1 2 3 3 2 1 4 1 2 0

dictionary = set()
result = []

for i in range(len(array)):


  if array[i] in dictionary:

  else:
    dictionary[array[i]] = 1


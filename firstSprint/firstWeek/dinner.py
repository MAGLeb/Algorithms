number = int(input())
array = sorted(map(int, input().split(' ')))
i = 0

while i != number:
  if i == number - 1:
    print(array[i])
    break
  
  if array[i] == array[i + 1]:
    i += 2
  else:
    print(array[i])
    break


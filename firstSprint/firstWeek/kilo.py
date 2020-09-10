# ids = [int(x) for x in input().split(' ')]
# k = int(input())
dictionary = {}
ids = [1,2,3,4,5,6,2,3,4,5,2,3,4,3,4,5,6,7,8,9]
k = 5

for item in ids:
  if(item in dictionary):
    dictionary[item] += 1
  else:
    dictionary[item] = 1

print(dictionary)

for item in sorted(dictionary, key=dictionary.get, reverse=True):
  if(k == 0):
    break
  k -= 1
  print(item),
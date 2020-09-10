f = open('leftNumber.txt', 'r')
number = int(f.readline())
first = sorted(map(int, f.readline().strip().split(' ')))

def leftNumber(first):
  for i in range(number - 1):

    if first[i] == first[i + 1]:
      return first[i]


print(leftNumber(first))
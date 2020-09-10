import random

f = open('A.txt', 'w')
f.write('5 \n')

for i in range(100):
  f.write(str(random.randrange(1000, 0, -1)) + ' ')


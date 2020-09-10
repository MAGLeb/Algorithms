import random
import runpy

for j in range(10):
  f = open('A.txt', 'w')

  for i in range(20):
    
    f.write(str(random.randrange(20, 0, -1)) + ' ')




  exec(open('I.py').read())
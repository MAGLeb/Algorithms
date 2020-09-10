filename = 'circle.txt'

f = open(filename, 'r')

visited_optional_courses = []

line = f.readline()

while True:
  line = f.readline().strip()

  if line == '':
    break

  if line not in visited_optional_courses:
    visited_optional_courses.append(line)

f.close()


f = open('output.txt', 'w')
for item in visited_optional_courses:
  f.write(item + '\n')

f.close()



